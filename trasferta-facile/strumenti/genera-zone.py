"""Genera le pagine per zona (zone/*.html), sitemap.xml e robots.txt.

Uso: python3 strumenti/genera-zone.py  (dalla cartella trasferta-facile)
Per aggiungere una zona basta aggiungere una voce a ZONE.
"""
from pathlib import Path

DOMINIO = "https://www.trasfertafacile.it"
RADICE = Path(__file__).resolve().parent.parent

ZONE = [
    {
        "file": "alloggi-operai-sesto-san-giovanni.html",
        "nome": "Sesto San Giovanni",
        "intro": "Sesto è uno dei comuni con più cantieri del nord di Milano: le ex aree industriali si stanno trasformando e le squadre arrivano a ondate, fase dopo fase. Ti troviamo un appartamento intero vicino al cantiere, collegato a Milano con la metro M1 e a pochi minuti dalla tangenziale.",
    },
    {
        "file": "alloggi-operai-cinisello-balsamo.html",
        "nome": "Cinisello Balsamo",
        "intro": "Cinisello è comoda per chi lavora tra Milano Nord, Monza e la Brianza: vicina all’A4 e a viale Fulvio Testi, con parcheggi più semplici che in città. È una delle zone dove troviamo più facilmente appartamenti adatti alle squadre.",
    },
    {
        "file": "alloggi-operai-bresso.html",
        "nome": "Bresso",
        "intro": "Bresso è la nostra base: siamo qui e vediamo ogni casa di persona. Tra Milano Nord, Cinisello, Cormano e Cusano, è un buon punto di partenza per cantieri in tutta la zona nord.",
    },
    {
        "file": "alloggi-operai-rho-fiera-milano.html",
        "nome": "Rho e Fiera Milano",
        "intro": "Prima di ogni grande fiera arrivano montatori e allestitori, e gli hotel intorno a Rho si riempiono o alzano i prezzi. Prenota per tempo un appartamento per la squadra: costi bassi, cucina e lavatrice anche nelle settimane di montaggio e smontaggio.",
    },
    {
        "file": "alloggi-operai-milano-nord.html",
        "nome": "Milano Nord",
        "intro": "Per cantieri a Niguarda, Bicocca, Greco e in tutta la zona nord di Milano cerchiamo appartamenti in città o appena fuori, dove i prezzi sono più bassi e il furgone si parcheggia più facilmente.",
    },
]

PAGINA = """<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Alloggi per operai a {nome} · Trasferta Facile</title>
<meta name="description" content="Appartamenti per squadre di operai e tecnici in trasferta a {nome}. Letti singoli, cucina, lavatrice, parcheggio per il furgone. Da €30 a persona a notte, proposta in 24 ore.">
<link rel="canonical" href="{dominio}/zone/{file}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%230f1115'/%3E%3Ccircle cx='24' cy='8' r='4' fill='%23ffd60a'/%3E%3Ctext x='14' y='23' font-family='Arial' font-weight='700' font-size='15' text-anchor='middle' fill='%23ffffff'%3ETF%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>

<header class="wrap nav">
  <a class="wordmark" href="../index.html"><i aria-hidden="true"></i>Trasferta Facile</a>
  <nav aria-label="Sezioni">
    <ul>
      <li><a href="../index.html#prezzi">Prezzi</a></li>
      <li><a href="../index.html#casa">La casa</a></li>
      <li><a href="../index.html#zone">Zone</a></li>
      <li><a href="../index.html#domande">Domande</a></li>
    </ul>
  </nav>
  <a class="btn" href="../index.html#richiesta">Chiedi una proposta</a>
</header>

<main>
  <div class="wrap">
    <p class="crumbs"><a href="../index.html">Trasferta Facile</a> · Zone · {nome}</p>
    <div class="zone-hero">
      <h1>Alloggi per operai a {nome}</h1>
      <p class="lead">{intro}</p>
      <div class="actions">
        <a class="btn" href="../index.html#richiesta">Richiedi una proposta <span class="arrow" aria-hidden="true">→</span></a>
        <a class="btn btn-light" href="../index.html#prezzi">Quanto risparmi</a>
      </div>
    </div>
  </div>

  <section class="wrap" aria-labelledby="cosa-title">
    <h2 id="cosa-title" class="sec-title">Cosa trovi in ogni casa</h2>
    <div class="split">
      <p class="sec-intro" style="margin-top:0">Appartamenti interi per squadre da 2 a 12 persone, per soggiorni da una settimana a diversi mesi. Da €30 a persona a notte, tutto incluso. Un solo referente e un solo documento per l’impresa.</p>
      <ul class="included">
        <li>Letti singoli<span>Uno per persona, niente divani letto.</span></li>
        <li>Cucina attrezzata<span>Per cucinare la sera e prepararsi il pranzo.</span></li>
        <li>Lavatrice<span>Le tute si lavano a casa.</span></li>
        <li>Parcheggio furgone<span>Posto auto o strada facile, indicato nella proposta.</span></li>
        <li>Utenze, wifi, biancheria<span>Tutto incluso, pulizia finale compresa.</span></li>
        <li>Chiavi anche all’alba<span>Arrivo concordato con voi, anche alle 6 del mattino.</span></li>
      </ul>
    </div>
  </section>

  <section class="wrap" aria-labelledby="come-title">
    <h2 id="come-title" class="sec-title">Come funziona</h2>
    <p class="sec-intro">Ci scrivi zona del cantiere, numero di persone, data di arrivo e durata. Entro 24 ore ricevi 2-3 proposte con foto, indirizzo e prezzo finale. Paghi con bonifico, per settimana o per mese.</p>
    <h2 class="sec-title" style="margin-top:96px">Altre zone</h2>
    <ul class="other-zones">
{altre}
    </ul>
  </section>
</main>

<footer class="wrap">
  <div class="foot-grid">
    <div>
      <p class="foot-cta">Hai una squadra in arrivo a {nome}?</p>
      <a class="btn" style="margin-top:24px" href="../index.html#richiesta">Richiedi una proposta <span class="arrow" aria-hidden="true">→</span></a>
    </div>
    <div><h3>Dove siamo</h3><p>Bresso (MI)<br>Milano Nord</p></div>
    <div><h3>Orari</h3><p>Lun-sab 7-20<br>Per chi è già in casa, sempre</p></div>
    <div><h3>Contatti</h3><p><a class="link" href="../index.html#richiesta">Richiedi una proposta</a></p></div>
  </div>
  <div class="legal"><span>© Trasferta Facile</span><span>P.IVA in fase di attivazione</span></div>
</footer>
</body>
</html>
"""


def main():
    cartella = RADICE / "zone"
    cartella.mkdir(exist_ok=True)
    for z in ZONE:
        altre = "\n".join(
            f'      <li><a href="{a["file"]}">{a["nome"]}</a></li>' for a in ZONE if a is not z
        )
        html = PAGINA.format(dominio=DOMINIO, altre=altre, **z)
        (cartella / z["file"]).write_text(html, encoding="utf-8")

    url = [f"{DOMINIO}/"] + [f"{DOMINIO}/zone/{z['file']}" for z in ZONE]
    righe = "\n".join(f"  <url><loc>{u}</loc></url>" for u in url)
    (RADICE / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{righe}\n</urlset>\n",
        encoding="utf-8",
    )
    (RADICE / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {DOMINIO}/sitemap.xml\n", encoding="utf-8"
    )
    print(f"Generate {len(ZONE)} pagine di zona, sitemap.xml e robots.txt")


if __name__ == "__main__":
    main()
