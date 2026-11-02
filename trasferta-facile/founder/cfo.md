# Nota del CFO (in parole semplici)

- **Cosa vendiamo, in numeri:** una "notte-posto letto gestita". L'impresa paga circa €30 a persona a notte al proprietario; a noi resta la fee di gestione del 30%, cioè **€9**. Tolti pulizie, biancheria, spostamenti e fondo emergenze, **ogni notte-letto lascia circa €6** (67%).
- **Costi fissi: circa €610 al mese**, quasi metà sono i contributi INPS che si pagano anche senza guadagnare. Per questo la partita IVA si apre solo quando le prenotazioni diventano ricorrenti.
- **Break-even: 4 posti letto occupati al giorno**, cioè un solo appartamento da 4 posti pieno. È una soglia bassa: il rischio vero non sono i costi, ma **trovare clienti e case**.
- **Cassa necessaria: circa €1.500** prima che il progetto si paghi da solo. Sta dentro il budget di €3.000.
- **La voce da tenere d'occhio è la rampa** (quanti posti letto riempiamo mese dopo mese). Con volumi dimezzati l'anno 1 resta in utile ma scende a circa €4.400 (what-if `--volume 0.5`).
- **Tre modi per migliorare il margine**, provati con lo strumento:
  1. fee al 30% invece del 25%: con il 25% (€7,50) l'utile dell'anno 1 scende da €16.041 a €10.191, quindi difendere il 30% vale circa €5.800;
  2. far pagare a parte pulizie e cambio biancheria all'impresa: toglie circa €1,86 di costi per notte-letto;
  3. riempire prima: ogni mese di anticipo nella rampa vale centinaia di euro, quindi agenzie per il lavoro e fiere prima di tutto.
- I numeri segnati "stima" vanno sostituiti con preventivi veri. Struttura fiscale, contributi e tasse vanno confermati con un commercialista.
- Gli importi sono ricavi della società **prima delle imposte**; in regime forfettario non si applica l'IVA. L'utile va diviso tra i soci.

# Unit economics: Trasferta Facile (alloggi per squadre in trasferta, Milano Nord)

Every number below comes from the input file. Nothing is looked up or guessed.

## One notte-posto letto gestita

| line | per notte-posto letto gestita |
| --- | ---: |
| Price | €9.00 |
| Pulizia finale (stima: 60 euro a soggiorno / 84 notti-letto medie) | -€0.71 |
| Cambio biancheria settimanale (stima: 8 euro a persona a settimana) | -€1.15 |
| Materiali di consumo e kit casa (stima) | -€0.30 |
| Spostamenti per consegne chiavi e controlli (stima) | -€0.40 |
| Fondo emergenze 5% della fee | -€0.45 |
| **Contribution** (what each notte-posto letto gestita leaves to pay the fixed costs) | **€5.99** (67%) |

## The margin that matters

Fixed costs: €610 a month (INPS gestione commercianti, forfettario con riduzione 35% (4.611,64/anno x 0,65 / 12) €250, Google Ads (circa 7 euro al giorno) €200, Servizio online per partita IVA forfettaria (stima) €40, Assicurazione RC professionale (stima 360 euro/anno) €30, Telefono Iliad, dominio, email (stima) €15, Carburante e trasporti fissi (stima) €75).

- **Break-even: 4 notti-posto letto gestite a day.** Below that you lose money every month.
- **Profit margin at your plan** (40 a day): **61%** of every sale, after every cost.
- Capacity: 60 a day.

## Year 1, month by month

| month | notti-posto letto gestite a day | revenue | profit | cumulative (after €604 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0 | €0 | -€610 | -€1,214 |
| 2 | 2 | €540 | -€251 | -€1,465 |
| 3 | 4 | €1,080 | €109 | -€1,356 |
| 4 | 6 | €1,620 | €468 | -€888 |
| 5 | 8 | €2,160 | €828 | -€60 |
| 6 | 10 | €2,700 | €1,187 | €1,127 |
| 7 | 12 | €3,240 | €1,546 | €2,673 |
| 8 | 14 | €3,780 | €1,906 | €4,579 |
| 9 | 16 | €4,320 | €2,265 | €6,844 |
| 10 | 18 | €4,860 | €2,625 | €9,469 |
| 11 | 20 | €5,400 | €2,984 | €12,453 |
| 12 | 20 | €5,400 | €2,984 | €15,437 |

- **Year 1 operating profit: €16,041** on €35,100 of revenue.
- After the €604 startup spend: €15,437.
- Startup money earned back: month 6.
- Cash you need before it pays for itself: **€1,465**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 61% | 4 | €16,041 |
| Price -10% | 57% | 4 | €12,531 |
| Volume -20% | 59% | 4 | €11,369 |
| Unit costs +15% | 56% | 4 | €14,280 |

No red flags in these numbers. They are only as good as the inputs: check every cost against a real quote.
