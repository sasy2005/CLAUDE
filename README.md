# 📊 Analisi Investimenti AI

Un sito a pagina singola (`index.html`) dove scrivi il nome di un'**azienda o di un ETF** e il tuo **budget**, e un bot basato su Claude cerca sul web i dati aggiornati e produce un'analisi completa per l'investimento a lungo termine (5–10 anni): voto pesato su 100, bull/bear case, peso consigliato in portafoglio, 3 alternative dello stesso settore (con pulsanti per approfondirle al volo), fonti e sintesi.

## Come metterlo online

### Opzione A — GitHub Pages (consigliata)

1. Vai su **Settings → Pages** di questo repository
2. In "Build and deployment" scegli **Deploy from a branch**
3. Seleziona il branch che contiene `index.html` e la cartella `/ (root)`, poi **Save**
4. Dopo 1–2 minuti il sito sarà su `https://<tuo-utente>.github.io/CLAUDE/`

### Opzione B — In locale

Scarica `index.html` e aprilo con un doppio clic in qualsiasi browser. Funziona tutto anche da file locale.

## Le due modalità (e quanto costano)

| Modalità | Costo | Cosa serve | Come funziona |
|---|---|---|---|
| 🆓 **Analizza gratis su Claude** | **Zero crediti API** | Un account [claude.ai](https://claude.ai) (va bene il piano gratuito) | Un clic apre claude.ai con il prompt già precompilato (azienda, budget, data) e lo copia anche negli appunti: attivi la ricerca web e invii |
| 🔍 **Analizza qui con API** | ~$0,15–0,55 per analisi (vedi sotto) | Una API key di Anthropic | Il sito chiama direttamente Claude con la ricerca web e mostra l'analisi in streaming nella pagina |

> 💡 **Se vuoi spendere zero, usa sempre la modalità gratis**: è la stessa identica analisi, fatta dal tuo abbonamento claude.ai invece che dai crediti API. La modalità API serve solo se preferisci tutto dentro la pagina (con storico, costi mostrati, download).

### Costi della modalità API per modello (stima per analisi)

| Modello | Stima con 4 ricerche web | Note |
|---|---|---|
| **Claude Sonnet 5** (default) | **~$0,25** | Qualità vicina a Opus a circa metà prezzo |
| Claude Opus 4.8 | ~$0,45 | Qualità massima |

Il sito mostra la stima **prima** di lanciare l'analisi, chiede conferma al primo utilizzo e a fine analisi mostra il costo effettivo calcolato sui token reali. Puoi ridurre ulteriormente il costo abbassando le ricerche web a 3 nelle impostazioni.

### Ottenere la API key (solo per la modalità API)

1. Crea un account su [console.anthropic.com](https://console.anthropic.com) e carica un po' di credito
2. Genera una chiave in [Settings → API keys](https://console.anthropic.com/settings/keys)
3. Incollala nelle **⚙️ Impostazioni** del sito (resta salvata solo nel tuo browser)

## Funzionalità

- **Follow-up con un clic**: dalle 3 alternative proposte nell'analisi vengono generati pulsanti "approfondisci" che precompilano una nuova analisi
- Analisi in streaming con stato in tempo reale (ragionamento, ricerche web eseguite, scrittura)
- Scelta tra investimento in **unica soluzione** o **PAC mensile** (cambia l'analisi di allocazione)
- Storico delle ultime analisi salvato nel browser, ricaricabile con un clic
- Copia dell'analisi o download in `.md`
- Tema chiaro/scuro automatico, funziona anche da smartphone

## Privacy e sicurezza

- La API key (se usata) è salvata **solo nel `localStorage` del tuo browser** e viene inviata **esclusivamente ad `api.anthropic.com`**
- Nessun server intermedio: la pagina è un singolo file HTML statico senza backend
- Le analisi salvate nello storico restano nel tuo browser

## File del repository

- [`index.html`](index.html) — il sito/bot completo (autonomo, nessuna dipendenza)
- [`prompt-analisi-investimento-azienda-etf.md`](prompt-analisi-investimento-azienda-etf.md) — il template del prompt originale, utilizzabile anche manualmente

---

> ⚠️ **Nota importante**: le analisi sono informative, generate da un'IA su dati pubblici, e **non costituiscono consulenza finanziaria personalizzata**. Prima di investire verifica sempre le fonti primarie (bilanci ufficiali, KIID/prospetti) e valuta la tua situazione personale: orizzonte temporale, tolleranza al rischio e diversificazione complessiva del portafoglio.
