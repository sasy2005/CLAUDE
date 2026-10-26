# Trasferta Facile

Progetto di business: alloggi per squadre di operai e tecnici in trasferta a Milano Nord (Bresso, Sesto San Giovanni, Cinisello Balsamo, Rho Fiera, Milano Nord). Il titolare è uno studente di Bresso; un possibile socio si occupa delle vendite al telefono. Budget iniziale circa €3.000. Si scrive e si parla in italiano.

## Modello deciso
- Prodotto: appartamenti interi per trasferte da 1 settimana a 3+ mesi, letti singoli, cucina, lavatrice, parcheggio furgone, utenze incluse. Prezzo indicativo €30 a persona a notte.
- Forma legale: property manager con **mandato con rappresentanza** del proprietario (contratto tipo Confcommercio Milano / Rescasa / CCIAA Milano). Mai provvigioni all'impresa per "presentare" il proprietario (sarebbe mediazione, serve l'abilitazione).
- Sotto i 30 giorni: locazione breve (CIN, Alloggiati Web, imposta di soggiorno se prevista). Oltre i 30 giorni: locazione ad uso foresteria intestata all'impresa.
- Soldi: l'impresa paga il proprietario con bonifico, in anticipo (a settimana o a mese); il proprietario paga la fee di gestione (circa 25-35%). Nessun anticipo di cassa da parte nostra.
- Partita IVA forfettaria (ATECO 68.32.01) solo quando le prenotazioni diventano ricorrenti: INPS commercianti costa circa €3.000/anno anche senza guadagni. Le prime prenotazioni di prova come attività occasionale.
- Garanzia ai clienti: se la casa diventa indisponibile, soluzione equivalente entro 24 ore o rimborso della parte non usata. Servono penale nel mandato, 1-2 residence di riserva, fondo emergenze del 5%.

## Canali di acquisizione
Imprese: Google (scheda Business, pagine di zona, Ads €5-10/giorno), Subito.it, gruppi Facebook, agenzie per il lavoro, allestitori di Fiera Milano, imprese "da trasferta" con sede fuori Lombardia.
Proprietari: gestori di affitti brevi (molte case con un accordo), annunci di affitto fermi, agenzie immobiliari, gruppi Facebook locali, volantini.

## File
- `index.html`, `assets/style.css`: sito (font Geist, sfondo bianco, accento giallo #ffd60a, niente sfumature/ombre).
- `zone/*.html`, `sitemap.xml`, `robots.txt`: generati da `python3 strumenti/genera-zone.py` (modificare lì, non a mano).
- `kit/kit-lancio.md`: annunci, testi Google Business e Ads, script per agenzie, allestitori, gestori, proprietari, calendario fiere Rho, piano delle prime due settimane.
- `kit/*.csv`: fogli contatti (esistono anche come Google Sheet nella cartella Drive "Trasferta Facile").

## Da completare
- Dominio: da comprare (verificare quale: trasfertafacile.it / .com). Aggiornare `DOMINIO` in `strumenti/genera-zone.py`, `canonical` e JSON-LD in `index.html`, poi rigenerare.
- Numero WhatsApp Business (SIM Iliad) ed email: costante `CONTATTI` in fondo a `index.html`.
- Foto vere degli appartamenti, P.IVA nel footer.
- Pubblicazione: Netlify o Cloudflare Pages (gratis) con il dominio puntato dai DNS del registrar.
