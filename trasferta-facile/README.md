# Trasferta Facile – sito

Sito statico, nessuna dipendenza da installare:

- `index.html`: la pagina principale
- `assets/style.css`: lo stile condiviso da tutte le pagine
- `zone/`: una pagina per zona (Sesto, Cinisello, Bresso, Rho Fiera, Milano Nord), utile per Google
- `sitemap.xml`, `robots.txt`: per i motori di ricerca
- `strumenti/genera-zone.py`: rigenera le pagine di zona, la sitemap e robots.txt (`python3 strumenti/genera-zone.py`)
- `kit/`: kit di lancio (annunci, Google, script) e fogli contatti da importare in Google Sheets

## Prima di pubblicare
Nello script in fondo a `index.html` completa:

```js
const CONTATTI = { whatsapp: "", email: "info@trasfertafacile.it" };
```

- `whatsapp`: numero in formato internazionale senza `+` né spazi (es. `393331234567`). Se è vuoto, i pulsanti aprono un'email.
- `email`: l'indirizzo reale.

Se il dominio non è `www.trasfertafacile.it`, cambialo in `strumenti/genera-zone.py` (variabile `DOMINIO`) e nel tag `canonical` di `index.html`, poi rilancia lo script.

Poi aggiorna nel footer "P.IVA in fase di attivazione" quando apri la partita IVA.

## Metterlo online (gratis)
1. Compra il dominio `trasfertafacile.it`.
2. Cloudflare Pages o Netlify: "Deploy manually", trascina la cartella `trasferta-facile`.
3. Collega il dominio dalle impostazioni del progetto.
