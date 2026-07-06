# 📊 Analisi Investimenti AI

Un sito a pagina singola (`index.html`) dove scrivi il nome di un'**azienda o di un ETF** e il tuo **budget**, e un bot basato su Claude cerca sul web i dati aggiornati e produce un'analisi completa per l'investimento a lungo termine (5–10 anni): voto pesato su 100, bull/bear case, peso consigliato in portafoglio, 3 alternative dello stesso settore, fonti e sintesi.

## Come usarlo

### Opzione A — Online con GitHub Pages (consigliata)

1. Vai su **Settings → Pages** di questo repository
2. In "Build and deployment" scegli **Deploy from a branch**
3. Seleziona il branch che contiene `index.html` e la cartella `/ (root)`, poi **Save**
4. Dopo 1–2 minuti il sito sarà su `https://<tuo-utente>.github.io/CLAUDE/`

### Opzione B — In locale

Scarica `index.html` e aprilo con un doppio clic in qualsiasi browser. Funziona tutto anche da file locale.

## Le due modalità

| Modalità | Cosa serve | Come funziona |
|---|---|---|
| **🔍 Analizza ora** | Una API key di Anthropic | Il sito chiama direttamente Claude con la ricerca web attiva e mostra l'analisi in tempo reale nella pagina |
| **📋 Copia prompt per Claude** | Niente (gratis con un account claude.ai) | Il sito genera il prompt già compilato con azienda, budget e data: lo incolli su [claude.ai](https://claude.ai) con la ricerca web attiva |

### Ottenere la API key (per la modalità automatica)

1. Crea un account su [console.anthropic.com](https://console.anthropic.com) e carica un po' di credito
2. Genera una chiave in [Settings → API keys](https://console.anthropic.com/settings/keys)
3. Incollala nelle **⚙️ Impostazioni** del sito (resta salvata solo nel tuo browser)

**Costo indicativo per analisi**: circa **$0,15–0,50** con Claude Opus 4.8 (il modello di default, qualità massima), meno con Sonnet 5. Il costo effettivo, con token e numero di ricerche web, viene mostrato in fondo a ogni analisi.

## Funzionalità

- Analisi in streaming con stato in tempo reale (ragionamento, ricerche web eseguite, scrittura)
- Scelta tra investimento in **unica soluzione** o **PAC mensile** (cambia l'analisi di allocazione)
- Storico delle ultime analisi salvato nel browser, ricaricabile con un clic
- Copia dell'analisi o download in `.md`
- Tema chiaro/scuro automatico, funziona anche da smartphone

## Privacy e sicurezza

- La API key è salvata **solo nel `localStorage` del tuo browser** e viene inviata **esclusivamente ad `api.anthropic.com`**
- Nessun server intermedio: la pagina è un singolo file HTML statico senza backend
- Le analisi salvate nello storico restano nel tuo browser

## File del repository

- [`index.html`](index.html) — il sito/bot completo (autonomo, nessuna dipendenza)
- [`prompt-analisi-investimento-azienda-etf.md`](prompt-analisi-investimento-azienda-etf.md) — il template del prompt originale, utilizzabile anche manualmente

---

> ⚠️ **Nota importante**: le analisi sono informative, generate da un'IA su dati pubblici, e **non costituiscono consulenza finanziaria personalizzata**. Prima di investire verifica sempre le fonti primarie (bilanci ufficiali, KIID/prospetti) e valuta la tua situazione personale: orizzonte temporale, tolleranza al rischio e diversificazione complessiva del portafoglio.
