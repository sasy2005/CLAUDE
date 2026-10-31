#!/usr/bin/env python3
"""
Cerca negozi intorno a Bresso con le Google Places API (New), filtra quelli
con poche recensioni e crea i giri di visita in ordine efficiente, con i link
di Google Maps pronti da aprire sul telefono.

Uso base:
    export GOOGLE_MAPS_API_KEY="la-tua-chiave"
    python3 cerca_negozi.py

Opzioni utili:
    --raggio 3            raggio in km dal punto di partenza (default 3)
    --partenza 45.5386,9.1872   punto di partenza dei giri (default: centro di Bresso)
    --max-recensioni 100  scarta chi ha più recensioni di così
    --per-giro 10         negozi per giro (10 = un solo link Google Maps per giro)
    --categorie barbiere,estetica   solo alcune categorie (vedi CATEGORIE sotto)
    --mezzo walking       walking | bicycling | driving (solo per i link Maps)
    --demo                dati finti, per provare il percorso senza chiave API

File creati nella cartella output/:
    negozi.json   lista completa (è quella da caricare nella dashboard)
    negozi.csv    stessa lista, apribile con Excel/Fogli
    giri.html     i giri con i link Google Maps, da aprire sul telefono
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import math
import os
import random
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

# Centro di Bresso (piazza Italia, circa)
PARTENZA_DEFAULT = (45.5386, 9.1872)

# Categoria (come appare nella dashboard) -> ricerche testuali su Google Maps.
# Più ricerche per categoria = più copertura; i doppioni vengono rimossi.
CATEGORIE: dict[str, list[str]] = {
    "barbiere": ["barbiere", "barber shop"],
    "parrucchiere": ["parrucchiere", "parrucchiera"],
    "estetica": ["centro estetico", "estetista", "nail bar", "ricostruzione unghie"],
    "tatuaggi": ["tatuatore", "tattoo studio"],
    "gelateria": ["gelateria"],
    "pasticceria": ["pasticceria"],
    "bar": ["bar caffetteria"],
    "pizzeria-asporto": ["pizzeria da asporto", "pizza al taglio", "kebab"],
    "officina": ["officina meccanica", "gommista", "carrozzeria"],
    "autolavaggio": ["autolavaggio"],
    "animali": ["toelettatura cani", "negozio animali"],
    "veterinario": ["veterinario"],
    "ottico": ["ottico"],
    "lavanderia": ["lavanderia"],
    "palestra": ["palestra", "studio pilates"],
    "esperienze": ["escape room", "paintball", "laser tag"],
}

# Nomi di catene: hanno il marketing centrale, inutile proporre la card.
CATENE = re.compile(
    r"mcdonald|burger king|starbucks|autogrill|carrefour|esselunga|coop\b|lidl|"
    r"eurospin|conad|pam\b|unes|tigota|acqua\s*&\s*sapone|kiko|douglas|sephora|"
    r"salmoiraghi|grandvision|vision\s*ottica|mcfit|virgin active|anytime fitness|"
    r"fit\s*express|jean louis david|franck provost|toni\s*&\s*guy|old wild west|"
    r"roadhouse|spizzico|rossopomodoro|arcaplanet|isola dei tesori|norauto|"
    r"midas|speedy|euronics|unieuro|mediaworld|\bq8\b|tamoil|\beni\b|\besso\b|\bagip\b|\bshell\b|"
    r"\bip\b|dropship",
    re.IGNORECASE,
)

API_URL = "https://places.googleapis.com/v1/places:searchText"
FIELD_MASK = ",".join(
    [
        "places.id",
        "places.displayName",
        "places.formattedAddress",
        "places.location",
        "places.rating",
        "places.userRatingCount",
        "places.googleMapsUri",
        "places.businessStatus",
        "places.primaryTypeDisplayName",
        "places.nationalPhoneNumber",
        "places.regularOpeningHours.weekdayDescriptions",
        "nextPageToken",
    ]
)


# --------------------------------------------------------------------------
# Geometria
# --------------------------------------------------------------------------

def distanza_km(a: tuple[float, float], b: tuple[float, float]) -> float:
    """Distanza in linea d'aria (haversine) in km."""
    lat1, lon1 = map(math.radians, a)
    lat2, lon2 = map(math.radians, b)
    dlat, dlon = lat2 - lat1, lon2 - lon1
    h = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    return 6371.0 * 2 * math.asin(math.sqrt(h))


def riquadri(centro: tuple[float, float], raggio_km: float, griglia: int):
    """Divide il quadrato che contiene il cerchio in griglia x griglia riquadri.
    Google restituisce al massimo 60 risultati per ricerca: dividere l'area
    evita di perdere negozi nelle categorie più dense (es. bar)."""
    lat, lon = centro
    dlat = raggio_km / 111.32
    dlon = raggio_km / (111.32 * math.cos(math.radians(lat)))
    lat0, lon0 = lat - dlat, lon - dlon
    passo_lat, passo_lon = 2 * dlat / griglia, 2 * dlon / griglia
    for i in range(griglia):
        for j in range(griglia):
            yield {
                "low": {"latitude": lat0 + i * passo_lat, "longitude": lon0 + j * passo_lon},
                "high": {"latitude": lat0 + (i + 1) * passo_lat, "longitude": lon0 + (j + 1) * passo_lon},
            }


# --------------------------------------------------------------------------
# Google Places
# --------------------------------------------------------------------------

def cerca(chiave: str, testo: str, rettangolo: dict) -> list[dict]:
    """Una ricerca testuale in un riquadro, con paginazione (max 60 risultati)."""
    risultati, token = [], None
    for _ in range(3):
        corpo = {
            "textQuery": testo,
            "languageCode": "it",
            "regionCode": "IT",
            "pageSize": 20,
            "locationRestriction": {"rectangle": rettangolo},
        }
        if token:
            corpo["pageToken"] = token
        req = urllib.request.Request(
            API_URL,
            data=json.dumps(corpo).encode(),
            headers={
                "Content-Type": "application/json",
                "X-Goog-Api-Key": chiave,
                "X-Goog-FieldMask": FIELD_MASK,
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                dati = json.load(r)
        except urllib.error.HTTPError as e:
            msg = e.read().decode(errors="replace")
            sys.exit(f"\nErrore da Google ({e.code}) cercando '{testo}':\n{msg}\n"
                     "Controlla che la chiave sia giusta e che 'Places API (New)' sia attiva.")
        risultati += dati.get("places", [])
        token = dati.get("nextPageToken")
        if not token:
            break
        time.sleep(1.5)  # il token di pagina diventa valido dopo un attimo
    return risultati


def comune_da_indirizzo(indirizzo: str) -> str:
    """'Via Roma 1, 20091 Bresso MI, Italia' -> 'Bresso'."""
    m = re.search(r"\b\d{5}\s+(.+?)\s+[A-Z]{2}\b", indirizzo or "")
    return m.group(1).strip() if m else ""


def normalizza(p: dict, categoria: str) -> dict:
    loc = p.get("location", {})
    indirizzo = p.get("formattedAddress", "")
    return {
        "id": p["id"],
        "nome": p.get("displayName", {}).get("text", "?"),
        "categoria": categoria,
        "tipoGoogle": p.get("primaryTypeDisplayName", {}).get("text", ""),
        "indirizzo": indirizzo,
        "zona": comune_da_indirizzo(indirizzo),
        "lat": loc.get("latitude"),
        "lng": loc.get("longitude"),
        "recensioni": p.get("userRatingCount", 0),
        "rating": p.get("rating"),
        "telefono": p.get("nationalPhoneNumber", ""),
        "orari": p.get("regularOpeningHours", {}).get("weekdayDescriptions", []),
        "mapsUrl": p.get("googleMapsUri", ""),
    }


def raccogli(chiave: str, categorie: list[str], centro, raggio_km: float, griglia: int) -> list[dict]:
    trovati: dict[str, dict] = {}
    for cat in categorie:
        for testo in CATEGORIE[cat]:
            n_prima = len(trovati)
            for rett in riquadri(centro, raggio_km, griglia):
                for p in cerca(chiave, testo, rett):
                    if p.get("businessStatus", "OPERATIONAL") != "OPERATIONAL":
                        continue
                    if p["id"] not in trovati:  # la prima categoria che lo trova vince
                        trovati[p["id"]] = normalizza(p, cat)
            print(f"  {cat:18} '{testo}': +{len(trovati) - n_prima}")
    return list(trovati.values())


def dati_demo(centro, raggio_km: float, n: int = 45) -> list[dict]:
    """Negozi finti sparsi nel raggio, solo per provare il calcolo dei giri."""
    random.seed(7)
    cats = list(CATEGORIE)
    out = []
    for i in range(n):
        ang, r = random.uniform(0, 2 * math.pi), raggio_km * math.sqrt(random.random())
        lat = centro[0] + (r / 111.32) * math.cos(ang)
        lng = centro[1] + (r / (111.32 * math.cos(math.radians(centro[0])))) * math.sin(ang)
        out.append({
            "id": f"demo-{i}", "nome": f"Negozio demo {i + 1}", "categoria": random.choice(cats),
            "tipoGoogle": "", "indirizzo": "", "zona": "Demo", "lat": lat, "lng": lng,
            "recensioni": random.randint(0, 250), "rating": round(random.uniform(3.5, 5.0), 1),
            "telefono": "", "orari": [], "mapsUrl": "",
        })
    return out


# --------------------------------------------------------------------------
# Percorso
# --------------------------------------------------------------------------

def percorso_vicino(punti: list[dict], partenza) -> list[dict]:
    """Ordine 'vado sempre al più vicino', poi migliorato con 2-opt."""
    rimasti, giro, attuale = punti[:], [], partenza
    while rimasti:
        prossimo = min(rimasti, key=lambda p: distanza_km(attuale, (p["lat"], p["lng"])))
        rimasti.remove(prossimo)
        giro.append(prossimo)
        attuale = (prossimo["lat"], prossimo["lng"])
    return due_opt(giro, partenza)


def lunghezza(giro: list[dict], partenza) -> float:
    pos, tot = partenza, 0.0
    for p in giro:
        tot += distanza_km(pos, (p["lat"], p["lng"]))
        pos = (p["lat"], p["lng"])
    return tot


def due_opt(giro: list[dict], partenza, max_passate: int = 50) -> list[dict]:
    """Inverte tratti del percorso finché accorcia (percorso aperto che parte da casa).
    Calcola solo la differenza di lunghezza di ogni inversione, con le distanze
    precalcolate: veloce anche con centinaia di negozi."""
    n = len(giro)
    if n < 3:
        return giro
    coord = [partenza] + [(p["lat"], p["lng"]) for p in giro]
    d = [[distanza_km(a, b) for b in coord] for a in coord]
    ordine = list(range(n + 1))  # 0 = partenza, fissa
    for _ in range(max_passate):
        migliorato = False
        for i in range(1, n):
            for k in range(i + 1, n + 1):
                a, b, c = ordine[i - 1], ordine[i], ordine[k]
                prima = d[a][b]
                dopo = d[a][c]
                if k < n:
                    e = ordine[k + 1]
                    prima += d[c][e]
                    dopo += d[b][e]
                if dopo < prima - 1e-9:
                    ordine[i:k + 1] = reversed(ordine[i:k + 1])
                    migliorato = True
        if not migliorato:
            break
    return [giro[j - 1] for j in ordine[1:]]


def crea_giri(negozi: list[dict], partenza, per_giro: int) -> list[list[dict]]:
    """Un percorso unico su tutti i negozi, tagliato a pezzi di per_giro tappe
    (pezzi consecutivi = zone compatte), poi ogni pezzo riottimizzato
    partendo da casa."""
    tutto = percorso_vicino(negozi, partenza)
    pezzi = [tutto[i:i + per_giro] for i in range(0, len(tutto), per_giro)]
    return [percorso_vicino(pezzo, partenza) for pezzo in pezzi]


def link_maps(tappe: list[dict], partenza, mezzo: str) -> list[str]:
    """Link Google Maps con al massimo 9 tappe intermedie + destinazione."""
    links = []
    origine = f"{partenza[0]},{partenza[1]}"
    for i in range(0, len(tappe), 10):
        blocco = tappe[i:i + 10]
        coord = [f"{p['lat']},{p['lng']}" for p in blocco]
        q = {
            "api": "1",
            "origin": origine,
            "destination": coord[-1],
            "travelmode": mezzo,
        }
        if len(coord) > 1:
            q["waypoints"] = "|".join(coord[:-1])
        links.append("https://www.google.com/maps/dir/?" + urllib.parse.urlencode(q, safe=",|"))
        origine = coord[-1]
    return links


# --------------------------------------------------------------------------
# Output
# --------------------------------------------------------------------------

def scrivi_html(giri, partenza, mezzo, percorso: Path):
    righe = []
    for n, giro in enumerate(giri, 1):
        km = lunghezza(giro, partenza)
        bottoni = "".join(
            f'<a class="btn" href="{html.escape(u)}" target="_blank">Apri in Google Maps'
            f'{f" (parte {i + 1})" if len(giro) > 10 else ""}</a>'
            for i, u in enumerate(link_maps(giro, partenza, mezzo))
        )
        tappe = "".join(
            f"<li><b>{html.escape(p['nome'])}</b> <span>{html.escape(p['categoria'])} · "
            f"{p['recensioni']} rec · {p['rating'] or '–'}★</span><br>"
            f"<small>{html.escape(p['indirizzo'])}</small></li>"
            for p in giro
        )
        righe.append(
            f"<section><h2>Giro {n}</h2><p>{len(giro)} negozi · circa {km:.1f} km in linea d'aria</p>"
            f"{bottoni}<ol>{tappe}</ol></section>"
        )
    percorso.write_text(
        "<!doctype html><meta charset=utf-8><meta name=viewport content='width=device-width'>"
        "<title>Giri negozi</title><style>body{font:15px system-ui;margin:0 auto;max-width:640px;"
        "padding:16px}section{border-bottom:1px solid #ddd;padding-bottom:12px}"
        ".btn{display:inline-block;margin:4px 6px 4px 0;padding:10px 14px;background:#1f5f4a;"
        "color:#fff;border-radius:8px;text-decoration:none}li{margin:6px 0}span,small{color:#666}"
        "</style><h1>Giri negozi</h1>" + "".join(righe),
        encoding="utf-8",
    )


def carica_env(percorso: Path):
    """Legge KEY=valore dal file .env accanto allo script, se esiste."""
    if not percorso.exists():
        return
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        riga = riga.strip()
        if riga and not riga.startswith("#") and "=" in riga:
            k, v = riga.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def main():
    carica_env(Path(__file__).parent / ".env")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--raggio", type=float, default=3.0)
    ap.add_argument("--partenza", default=f"{PARTENZA_DEFAULT[0]},{PARTENZA_DEFAULT[1]}")
    ap.add_argument("--max-recensioni", type=int, default=100)
    ap.add_argument("--min-recensioni", type=int, default=0,
                    help="scarta le schede quasi vuote (spesso attività chiuse o senza negozio)")
    ap.add_argument("--per-giro", type=int, default=10)
    ap.add_argument("--categorie", default=",".join(CATEGORIE))
    ap.add_argument("--griglia", type=int, default=2, help="riquadri per lato (2 = 4 riquadri)")
    ap.add_argument("--mezzo", default="walking", choices=["walking", "bicycling", "driving"])
    ap.add_argument("--uscita", default=str(Path(__file__).parent / "output"))
    ap.add_argument("--demo", action="store_true")
    ap.add_argument("--usa-cache", action="store_true", help="riusa output/grezzi.json invece di chiamare Google")
    a = ap.parse_args()

    partenza = tuple(float(x) for x in a.partenza.split(","))
    categorie = [c.strip() for c in a.categorie.split(",") if c.strip()]
    sconosciute = [c for c in categorie if c not in CATEGORIE]
    if sconosciute:
        sys.exit(f"Categorie sconosciute: {sconosciute}. Disponibili: {', '.join(CATEGORIE)}")

    grezzi = Path(__file__).parent / "output" / "grezzi.json"
    if a.demo:
        tutti = dati_demo(partenza, a.raggio)
    elif a.usa_cache:
        tutti = json.loads(grezzi.read_text(encoding="utf-8"))
        print(f"Uso {len(tutti)} negozi salvati in {grezzi}")
    else:
        chiave = os.environ.get("GOOGLE_MAPS_API_KEY")
        if not chiave:
            sys.exit("Manca la chiave: export GOOGLE_MAPS_API_KEY=\"...\" (oppure usa --demo)")
        print(f"Cerco in un raggio di {a.raggio} km da {partenza}...")
        tutti = raccogli(chiave, categorie, partenza, a.raggio, a.griglia)
        grezzi.parent.mkdir(parents=True, exist_ok=True)
        grezzi.write_text(json.dumps(tutti, ensure_ascii=False), encoding="utf-8")

    negozi = [
        n for n in tutti
        if n["lat"] is not None
        and distanza_km(partenza, (n["lat"], n["lng"])) <= a.raggio
        and a.min_recensioni <= n["recensioni"] <= a.max_recensioni
        and n["categoria"] in categorie
        and not CATENE.search(n["nome"])
    ]
    print(f"\nTrovati {len(tutti)} negozi, {len(negozi)} con al massimo {a.max_recensioni} recensioni.")
    if not negozi:
        sys.exit("Nessun negozio da visitare con questi filtri.")

    giri = crea_giri(negozi, partenza, a.per_giro)
    for g, giro in enumerate(giri, 1):
        for o, p in enumerate(giro, 1):
            p["giro"], p["ordine"] = g, o

    out = Path(a.uscita)
    out.mkdir(parents=True, exist_ok=True)
    ordinati = [p for giro in giri for p in giro]
    (out / "negozi.json").write_text(json.dumps(ordinati, ensure_ascii=False, indent=1), encoding="utf-8")
    with open(out / "negozi.csv", "w", newline="", encoding="utf-8") as f:
        campi = ["giro", "ordine", "nome", "categoria", "zona", "recensioni", "rating",
                 "indirizzo", "telefono", "mapsUrl", "lat", "lng", "id"]
        w = csv.DictWriter(f, fieldnames=campi, extrasaction="ignore")
        w.writeheader()
        w.writerows(ordinati)
    scrivi_html(giri, partenza, a.mezzo, out / "giri.html")

    print(f"{len(giri)} giri da massimo {a.per_giro} negozi. File in {out}/")
    for g, giro in enumerate(giri, 1):
        print(f"  Giro {g:2}: {len(giro):2} negozi, {lunghezza(giro, partenza):4.1f} km")


if __name__ == "__main__":
    main()
