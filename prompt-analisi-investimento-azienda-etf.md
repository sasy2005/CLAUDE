# Prompt: Analisi Investimento Azienda/ETF

Copia e incolla questo prompt in Claude (con web search attivo) sostituendo `[NOME_AZIENDA_O_ETF]` e `[BUDGET]` con i tuoi dati.

---

Sei un analista finanziario indipendente. Devo valutare se investire A LUNGO TERMINE (orizzonte 5-10 anni) in: **[NOME_AZIENDA_O_ETF]**.

Il mio budget disponibile per questo investimento è: **[BUDGET]€** (indica anche se è l'intero capitale che vuoi investire ora o una cifra mensile/ricorrente, es. PAC).

Prima di rispondere, cerca sul web informazioni AGGIORNATE A OGGI su:
1. Dati fondamentali dell'azienda/ETF (ricavi, utili, crescita, debito, margini, valutazione P/E o P/S rispetto ai competitor e alla media storica)
2. Notizie macroeconomiche recenti rilevanti (tassi d'interesse, inflazione, politiche monetarie, geopolitica) che possono impattare il settore
3. Trend specifici del settore in cui opera (domanda, regolamentazione, tecnologia, competizione)
4. Notizie recenti specifiche sull'azienda/ETF (ultimi risultati trimestrali, guidance, eventi rilevanti)
5. Se è un ETF: TER (costo annuo), tipo di replica (fisica/sintetica), paese di domiciliazione (rilevante per fiscalità italiana), concentrazione nelle prime 10 holding, AUM (patrimonio gestito — sotto certe soglie c'è rischio chiusura del fondo)

Poi fornisci l'analisi in questo formato esatto:

## 1. Punteggio finale
**Voto: X/100** (dove 100 = investimento a lungo termine ottimo, 1 = da evitare)

Mostra anche il dettaglio dei pesi usati per calcolarlo:
- Fondamentali (30%): X/100
- Valutazione attuale (25%): X/100
- Rischio macro/settoriale (25%): X/100
- Momentum e vantaggio competitivo (20%): X/100

**Livello di confidenza del voto**: Alto / Medio / Basso (in base a quanti dati affidabili hai trovato)

## 2. Bull case (perché potrebbe andare bene)
3-4 punti diretti sui motivi per cui questo investimento potrebbe performare bene nel lungo periodo.

## 3. Bear case (perché potrebbe andare male)
3-4 punti diretti su rischi concreti, red flag, o motivi di cautela.

## 4. Peso consigliato nel portafoglio
In base al voto, al livello di rischio implicito e al budget di [BUDGET]€, suggerisci:
- Che percentuale del budget indicato avrebbe senso allocare a questo singolo asset (in un portafoglio diversificato, non "tutto qui")
- L'importo indicativo in euro corrispondente
- Se ha senso investire in un'unica soluzione o gradualmente (PAC/DCA) vista la situazione attuale di mercato
- Un'avvertenza chiara se il budget indicato è troppo concentrato su un singolo titolo/settore rispetto a una diversificazione sana

## 5. Confronto rapido con 3 alternative dello stesso settore
Identifica le 3 aziende/ETF più simili o comparabili a [NOME_AZIENDA_O_ETF] nello stesso settore/tema, e per ciascuna dai SOLO:
- Nome
- Voto/100
- Una riga di motivazione (max 20 parole)

## 6. Fonti principali usate
Elenca 2-4 fonti concrete su cui ti sei basato (es. ultimo bilancio/10-Q, articolo di settore, dato macro specifico), con data.

## 7. Sintesi finale
2-3 righe con la tua raccomandazione netta: che senso ha investirci oggi, con quel budget, rispetto alle alternative individuate.

---

**Nota su freschezza dati**: indica sempre "Analisi basata su dati disponibili fino al [data odierna]" in cima alla risposta.

**Follow-up**: se in seguito chiedo di approfondire una delle 3 alternative, applica la stessa analisi completa (punti 1-7) anche a quella.

**Nota importante**: questa è un'analisi informativa basata su dati pubblici, non una consulenza finanziaria personalizzata. Prima di investire, verifica sempre le fonti primarie (bilanci ufficiali, comunicati aziendali) e valuta la tua situazione personale (orizzonte temporale, tolleranza al rischio, diversificazione complessiva del portafoglio, non solo di questo singolo investimento).
