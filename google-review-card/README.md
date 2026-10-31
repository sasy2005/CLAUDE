# Google Review Card: kit di vendita

| File | A cosa serve |
|---|---|
| `playbook.md` | Prezzi, target, le 4 strategie con i pitch, risposte alle obiezioni |
| `cerca_negozi.py` | Il bot: cerca i negozi su Google Maps intorno a Bresso, tiene quelli con poche recensioni e crea i giri in ordine efficiente |
| `dashboard.html` | La dashboard da usare sul telefono durante i giri (pubblicata su claude.ai, i dati restano salvati lì) |

## 1. Creare la chiave Google (una volta, circa 5 minuti)

1. Vai su <https://console.cloud.google.com> con il tuo account Google e crea un progetto (es. "review-card").
2. Nel menu: **API e servizi → Libreria**, cerca **Places API (New)** e premi **Abilita**.
3. Ti chiederà un **account di fatturazione** (serve la carta). Con il nostro uso **non paghi niente**: Google dà ogni mese un numero di chiamate gratuite e una ricerca completa ne usa circa 150-250.
4. **API e servizi → Credenziali → Crea credenziali → Chiave API**. Copia la chiave.
5. Sulla chiave appena creata: **Limitazioni API → Limita chiave → Places API (New)**. Così, se qualcuno la trova, non può usarla per altro.
6. Per sicurezza, in **Places API (New) → Quote** metti un limite giornaliero (es. 500 richieste al giorno).

## 2. Lanciare il bot

```bash
export GOOGLE_MAPS_API_KEY="la-tua-chiave"
```

```bash
python3 cerca_negozi.py --raggio 3 --max-recensioni 100
```

Crea nella cartella `output/`:
- `negozi.json`, da caricare nella dashboard;
- `negozi.csv`, da aprire con Excel o Fogli;
- `giri.html`, i giri con i bottoni "Apri in Google Maps".

Opzioni: `--categorie barbiere,estetica,officina` per cercare solo alcune categorie, `--per-giro 10`, `--partenza lat,lng` per partire da casa tua, `--mezzo bicycling`, `--demo` per una prova senza chiave.

## 3. Dashboard

- Ogni giro ha il bottone **Apri in Maps** con i negozi ancora da visitare, nell'ordine giusto.
- Tocchi un negozio e segni la visita: strategia (la dashboard ti suggerisce quella meno usata per quella categoria, così il test resta equilibrato), con chi hai parlato, esito, recensioni, obiezione.
- Le prove lasciate finiscono in **Ritorni** con la data. Al ritorno segni le recensioni nuove e se ha comprato.
- In **Risultati** trovi la conversione per strategia, categoria, zona e interlocutore, le obiezioni, l'incasso e le card rimaste.
- Per l'analisi basta dirlo a Claude, che legge i dati direttamente.
