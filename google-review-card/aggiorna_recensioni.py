#!/usr/bin/env python3
"""
Legge il numero attuale di recensioni su Google per una lista di negozi.

Uso:
    python3 aggiorna_recensioni.py ids.txt > aggiornate.json

ids.txt contiene un place id di Google per riga (quelli dei clienti e dei
negozi in prova). La chiave viene letta dallo stesso file usato da
cerca_negozi.py. Ogni negozio costa una chiamata Place Details.
"""

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

from cerca_negozi import carica_env

carica_env(Path(__file__).parent / ".env")
chiave = os.environ.get("GOOGLE_MAPS_API_KEY")
if not chiave:
    sys.exit("Manca la chiave Google")

out = {}
for pid in Path(sys.argv[1]).read_text().split():
    if pid.startswith("m-"):
        continue  # negozio aggiunto a mano, non ha un id Google
    req = urllib.request.Request(
        f"https://places.googleapis.com/v1/places/{pid}",
        headers={"X-Goog-Api-Key": chiave, "X-Goog-FieldMask": "id,userRatingCount,rating"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.load(r)
        out[pid] = {"data": date.today().isoformat(), "rec": d.get("userRatingCount", 0), "rating": d.get("rating")}
    except urllib.error.HTTPError as e:
        print(f"{pid}: errore {e.code}", file=sys.stderr)
json.dump(out, sys.stdout, indent=1)
