# Trasferta Facile – sito

Sito di una pagina (`index.html`, nessuna dipendenza da installare).

## Prima di pubblicare
Nello script in fondo a `index.html` completa:

```js
const CONTATTI = { whatsapp: "", email: "info@trasfertafacile.it" };
```

- `whatsapp`: numero in formato internazionale senza `+` né spazi (es. `393331234567`). Se è vuoto, i pulsanti aprono un'email.
- `email`: l'indirizzo reale.

Poi aggiorna nel footer "P.IVA in fase di attivazione" quando apri la partita IVA.

## Metterlo online (gratis)
1. Compra il dominio `trasfertafacile.it`.
2. Cloudflare Pages o Netlify: "Deploy manually", trascina la cartella `trasferta-facile`.
3. Collega il dominio dalle impostazioni del progetto.
