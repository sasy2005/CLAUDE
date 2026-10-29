# 🗂️ La mia Dashboard — email, calendario e cose da fare (con la voce)

Una dashboard personale in un **unico file** (`index.html`) che:

- 📬 **legge le email** dell'account universitario e le divide in **«Per te»** (scritte proprio a te) e **«Broadcast»** (inviate a tutto il corso, liste, newsletter, avvisi automatici), mostrando il motivo della classificazione
- ✍️ **prepara le bozze di risposta** per le email dirette e le salva nelle **Bozze di Gmail**, **senza mai inviare niente**
- 📌 trova nelle email **scadenze e cose da fare** (iscrizioni, consegne, documenti…) e te le propone con un clic
- ✅ ordina le **cose da fare per importanza** (🔥 Urgente / ⭐ Importante / 🌱 Quando puoi) in base a scadenza, priorità e parole chiave (esame, consegna, tasse…)
- 📅 mostra il **calendario** dei prossimi giorni, con le scadenze delle attività; gli impegni sono **colorati per importanza** (🔴 molto importante, 🟡 importante, nessun colore = normale)
- 🗓️ ha **«La mia giornata»**: la sera programmi il giorno dopo a blocchi orari (es. `10-14 università`, `15-17 palestra`), il giorno dopo vedi cosa stai facendo *adesso*, quanto manca e i buchi liberi
- ☀️ ogni **mattina** ti accoglie con un **recap**: programma della giornata, impegni importanti, cose urgenti, email da leggere e bozze pronte (con la chiave Gemini anche un breve riassunto scritto dall'AI). Premi «🔊 Leggimelo» per ascoltarlo
- 🎓 mostra l'**orario delle lezioni** preso da Google Calendar: le lezioni che non segui le **nascondi** (o le elimini) con un tocco
- ⏳ tiene il **countdown degli esami**
- ✨ la sera ti **propone la giornata di domani** dopo aver imparato la tua routine (non chiede niente le prime volte)
- 💪 tiene traccia di **abitudini e sport** (palestra, beach volley, lettura…) con obiettivo settimanale e serie di settimane di fila
- 🔔 manda **notifiche** prima di impegni e attività
- 📲 si **installa come app** sul telefono e **si sincronizza** tra PC e telefono
- 🎙️ si comanda **a voce** (o scrivendo) in italiano, anche per **rispondere alle email**, **archiviarle** o **segnarle come lette**
- 💸 è **tutto gratis**: niente server, niente abbonamenti; i dati restano nel tuo browser e nel tuo Google Drive

Apri la pagina e vedi subito tutto con **dati di esempio**; poi colleghi il tuo account.

---

## 🎙️ Comandi vocali

Premi il microfono (o `Ctrl+M`) e parla. Esempi:

| Cosa vuoi fare | Cosa dire |
|---|---|
| Segnare come fatta un'attività | «ho finito la relazione di fisica», «ho pagato la seconda rata» |
| Eliminare un'attività | «cancella il quaderno» |
| Aggiungere un'attività | «aggiungi studiare analisi entro venerdì urgente», «ricordami di chiamare la segreteria il 3 novembre» |
| Aggiungere al calendario | «segna in calendario ricevimento con il prof domani alle 15», «fissa riunione di gruppo giovedì alle 3 per 2 ore» |
| Scrivere un'email | «manda una email a Giulia dicendo che porto io gli appunti» → si apre l'email pronta; poi di' **«conferma»** per inviarla, **«salva»** per lasciarla in bozza o **«annulla»** |
| Organizzare la giornata | «programma domani dalle 10 alle 14 università, 15 17 palestra, 19 21 beach volley, 23 23:30 libro» |
| Sentire il programma | «cosa ho in programma domani?», «com'è la mia giornata?» |
| Recap del mattino | «recap», «buongiorno» |
| Evento importante | «segna in calendario esame di fisica venerdì alle 9 molto importante» |
| Farsi proporre la giornata | «organizzami domani» → poi «accetta» |
| Abitudini | «sono andato in palestra», «ho letto», «ho fatto beach volley» |
| Esami | «aggiungi esame di analisi il 15 gennaio alle 9», «quanto manca agli esami?» |
| Rispondere a un'email | «rispondi ad Auretta che va bene giovedì alle 10» → controlli e dici «conferma» o «salva» |
| Archiviare / segnare letta | «archivia la mail della mensa», «segna come letta la mail di Giulia», «segna tutte le broadcast come lette» |
| Sapere cosa fare | «cosa devo fare oggi?», «che impegni ho domani?», «ho nuove email?» |
| Altro | «aggiorna», «aiuto» |

Capisce date come *oggi, domani, dopodomani, venerdì, il 12 dicembre, 5/11, tra 3 giorni* e orari come *alle 15, alle 15:30, alle 8 di sera*.
Il riconoscimento vocale è quello gratuito del browser: funziona su **Chrome, Edge e Safari** (su Firefox puoi scrivere i comandi).

> 🔒 Le email partono **solo** quando premi «Invia» o dici «conferma». Le bozze automatiche non vengono mai inviate.

---

## 🚀 Messa online (gratis, 2 minuti)

Il login Google non funziona aprendo il file dal disco: serve un indirizzo web.

1. Su GitHub vai in **Settings → Pages** di questo repository
2. **Deploy from a branch** → scegli il branch `claude/friendly-goodall-vbrqrk` → cartella `/ (root)` → **Save**
3. Dopo un paio di minuti la dashboard è su **`https://sasy2005.github.io/CLAUDE/dashboard/`**

(In alternativa, sul tuo PC: `python3 -m http.server 8000` nella cartella del repo e apri `http://localhost:8000/dashboard/`.)

---

## 🔗 Collegare l'account universitario (Google) — una volta sola, ~5 minuti

Molte università usano Google Workspace (Gmail) per la posta degli studenti. Serve un "Client ID" gratuito:

1. Vai su [console.cloud.google.com](https://console.cloud.google.com) (puoi usare anche il tuo Gmail personale) e crea un **nuovo progetto**, es. "Dashboard"
2. **API e servizi → Libreria**: abilita **Gmail API**, **Google Calendar API** e **Google Drive API**
3. **API e servizi → Schermata consenso OAuth** (o "Google Auth Platform"):
   - tipo utente **Esterno**, nome app "Dashboard", la tua email come contatto
   - nella sezione **Utenti di test / Pubblico** aggiungi la tua **email universitaria**
   - lascia l'app in modalità **Test** (non serve nessuna verifica, è gratis)
4. **API e servizi → Credenziali → Crea credenziali → ID client OAuth**:
   - tipo **Applicazione web**
   - **Origini JavaScript autorizzate**: `https://sasy2005.github.io` (e `http://localhost:8000` se la usi in locale)
5. Copia il **Client ID** (finisce con `.apps.googleusercontent.com`)
6. Nella dashboard: **⚙️ Impostazioni** → incolla il Client ID, scrivi la tua email universitaria → **Salva** → **Collega account**

Al primo accesso Google mostrerà l'avviso "app non verificata": è normale, l'app è la tua → *Avanzate → Vai a Dashboard*.
Google dà alle pagine web accessi di un'ora. La dashboard li **rinnova da sola**: quando l'accesso sta per scadere, al primo clic o tasto si apre e si chiude da sola una finestrella di Google, senza chiederti niente.

Permessi richiesti: lettura email e gestione delle etichette (segnare come letta / archiviare), creazione bozze/invio (solo quando confermi tu), lettura dei tuoi calendari e aggiunta di eventi, una cartella privata dell'app su Google Drive per la sincronizzazione.

### ⚠️ Se l'università blocca l'accesso

Alcuni atenei impediscono alle app esterne di accedere agli account studenti (errore tipo *"accesso bloccato dall'amministratore"*). Soluzioni gratuite:

- **Inoltro automatico**: nel webmail dell'università imposta l'inoltro verso un tuo Gmail personale e collega quello alla dashboard (indica l'email universitaria in *Altri tuoi indirizzi*, così la classificazione "per te / broadcast" continua a funzionare)
- Se la tua università usa **Outlook / Microsoft 365** invece di Gmail, la dashboard va adattata a Microsoft Graph (stessa idea, login diverso)

---

## ✨ Intelligenza artificiale (opzionale, gratis)

Senza AI la dashboard funziona già: classificazione, bozze "a modello", scadenze e comandi vocali si basano su regole.
Con una chiave **Google Gemini** (piano gratuito) diventa più intelligente:

- riassunti delle email e bozze di risposta scritte su misura, nel tono giusto (formale col prof, informale con i compagni)
- estrazione precisa di attività e scadenze
- comandi vocali più liberi (es. «scrivi al prof Bianchi che domani arrivo 10 minuti in ritardo» → email completa ed educata)

Come fare: crea la chiave su [aistudio.google.com/apikey](https://aistudio.google.com/apikey) → incollala in **⚙️ Impostazioni → Chiave API Google Gemini** → «Prova la chiave».
La dashboard rispetta i limiti del piano gratuito (una richiesta ogni ~5 secondi, massimo 15 email analizzate per aggiornamento; i risultati restano in memoria).

> Nota privacy: con la chiave attiva il testo delle email viene inviato a Google Gemini per l'analisi. Nel piano gratuito Google può usare questi dati per migliorare i suoi servizi. Se non vuoi, lascia il campo vuoto e usa le regole base.

---

## 🎨 Importanza degli impegni

Il colore viene deciso così (il primo che vale):

1. quello che scegli tu: **tocca un evento** e scegli normale / importante / molto importante
2. il colore dato all'evento in Google Calendar (rosso/rosa = molto importante, arancio/giallo = importante)
3. le parole nel titolo: *esame, prova, appello, scritto, orale, laurea, tesi, consegna, scadenza, visita…* = molto importante; *ricevimento, riunione, incontro, appuntamento, presentazione, seminario…* = importante
4. tutto il resto (lezioni, palestra, ecc.) resta **senza colore**

Gli impegni importanti dei prossimi 3 giorni finiscono nel recap del mattino.

## 🗓️ La mia giornata — come scriverla

Un'attività per riga, oppure tutto di fila; vanno bene tutti questi formati:

```
10-14 università
15:30-17 palestra
dalle 19 alle 21 beach volley
23 23:30 libro
università dalle 10 alle 14, palestra dalle 15 alle 17
```

Dopo le 19 la sezione si apre direttamente su **Domani**. Gli orari dopo mezzanotte (es. `22-1 film`) sono gestiti. Le attività prendono un'icona e un colore in automatico (studio, sport, svago, casa, lavoro).

## 🎓 Orario delle lezioni

**Università di Milano-Bicocca (orario EasyStaff, «Cerca il tuo orario per corso di studio»):**

1. Nella pagina dell'orario, in **«Lista insegnamenti»** togli la spunta ai corsi che **non segui**
2. Premi **«Esporta sul tuo calendario»**: scarica un file `.ics` con le lezioni selezionate
3. Su PC apri [Google Calendar](https://calendar.google.com) con l'account universitario:
   - a sinistra, accanto ad **«Altri calendari»**, premi **+ → Crea nuovo calendario** → nome **«Lezioni»** → Crea
   - poi **⚙️ Impostazioni → Importa ed esporta → Importa**: scegli il file `.ics` e come calendario **«Lezioni»** → **Importa**
4. La dashboard trova da sola il calendario «Lezioni» (o sceglilo in ⚙️ Impostazioni → Calendario delle lezioni)

Il file è una copia: se l'orario cambia, elimina il calendario «Lezioni» e ripeti l'importazione.
Siccome le lezioni stanno in un calendario tuo, dalla dashboard puoi anche **eliminarle davvero** («Elimina tutti i …») oppure solo **nasconderle** («Non seguo questo corso»).

**Altre università:** se il sito dell'orario dà un **link** iCal invece di un file, usa in Google Calendar **Altri calendari → + → Da URL**.

## ✨ «Organizzami domani»

Ogni giornata che salvi viene ricordata (4 mesi). Quando ha visto **almeno 2 volte** lo stesso giorno della settimana, la sera la dashboard ti propone da sola la giornata di domani:
le attività che fai di solito quel giorno (🔁), le lezioni e gli impegni del calendario (🎓 📅) e la cosa più urgente in un buco libero (⏰).
Puoi accettarla, modificarla o chiedere all'AI di migliorarla. Le prime volte non propone niente.

## 🔔 Notifiche e 📲 app sul telefono

- **Notifiche**: ⚙️ Impostazioni → Notifiche → attiva e scegli quanti minuti prima. Arrivano finché la dashboard è aperta (anche in un'altra scheda o come app installata).
- **Telefono a dashboard chiusa**: attiva «Copia La mia giornata su Google Calendar»: i blocchi della giornata finiscono nel calendario (in grigio) e l'app Google Calendar del telefono ti avvisa.
- **Installare l'app**: Android/Chrome → menu ⋮ → **Installa app** (o il pulsante «📲 Installa» in alto); iPhone/Safari → **Condividi → Aggiungi alla schermata Home**.
- **Sincronizzazione PC ↔ telefono**: cose da fare, giornata, abitudini, esami e impostazioni vengono salvati in una cartella nascosta del tuo Google Drive visibile solo a questa app.
  Serve abilitare la **Google Drive API** nel progetto Google Cloud (API e servizi → Libreria → «Google Drive API» → Abilita).

> Dopo questo aggiornamento la dashboard chiede **un permesso in più** a Google (archiviare email, leggere tutti i calendari, Drive dell'app): compare un avviso viola, premi **«Dai il permesso»**.

## 🧠 Come capisce se un'email è «per te» o «broadcast»

È **broadcast** se vale almeno una di queste condizioni (il motivo è mostrato sull'email):

- ha intestazioni da mailing list / newsletter (`List-Id`, `List-Unsubscribe`, `Precedence: bulk`)
- il tuo indirizzo **non** è tra i destinatari "A" o "Cc" (eri in Ccn o arrivava da una lista)
- ha 6 o più destinatari
- il mittente è automatico (`noreply`, `newsletter`, notifiche…)
- è indirizzata a un gruppo (`studenti-…`, `tutti@`, `corso…`, `iscritti…`)

Altrimenti è **per te**. Per le email "per te" non lette che contengono una domanda o una richiesta, viene preparata la bozza.

## 🔐 Privacy

- Nessun server: la pagina parla direttamente con Google dal tuo browser
- Client ID e chiave Gemini sono salvati nel `localStorage` del tuo browser; attività, giornate, abitudini, esami e impostazioni anche nella cartella privata dell'app sul tuo Google Drive (per la sincronizzazione)
- Le email non vengono salvate (solo i riassunti AI, per non rifare le stesse richieste)
- Le attività si possono anche esportare/importare in JSON da **⚙️ Impostazioni → Dati**
