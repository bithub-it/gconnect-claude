---
name: gconnect-shopping-sku-economics
description: Classifica SKU Shopping per costo, ordini reali, ROAS, opportunità, prodotti da escludere e sensibilità prezzo/margine.
---
# Redditività Shopping per SKU: niente conversioni di facciata

> **Strumenti GConnect da preferire** (usa solo quelli presenti nell'elenco degli strumenti disponibili e rispetta i loro parametri): `ads_products`, `mapped_product`, `unified_product_history`, `product_diagnostics`, `merchant_products`, `merchant_organic_performance` (schede gratuite) e `google_read_query` per le segmentazioni supportate. Se uno strumento manca o risponde «non autorizzato», dichiaralo e non aggirare il blocco.

## Metodo
- Partire dal profilo preferenze e dalla strategia di offerta: Manual CPC, massimizza conversioni, CPA target, massimizza valore, ROAS target, vincolo budget, campagne con gruppi di prodotti/PMax. Chiedere *margine minimo* e *ROAS break-even* se non presenti; non inventare margini.
- Query Shopping per SKU con cost, clicks, impressions, conversions e conversions_value, segmentazione per campagna/gruppo e conversion action quando supportata. Le conversioni attribuite a chiamate, indicazioni, `add_to_cart`, `begin_checkout`, visite o lead non sono ordini. Mostrare separatamente il totale Ads e il totale *purchase-only* verificato. Evitare doppio conteggio GA4-import Ads e tag Ads.
- Mappare SKU per identificatori esatti verificati tra Ads/Merchant/GA4 (`mapped_product`, `unified_product_history` quando disponibili). Non aggregare SKU omonimi, varianti, currency diverse, offerte di paese diverso o ID inferiti.
- Calcolare: costo per ordine attribuito = costo Ads / ordini attribuiti; ROAS acquisti = valore acquisti attribuiti / costo Ads; costo per nuovo cliente **solo** con dati di nuovo cliente attendibili; margine dopo Ads **solo** con costo prodotto, logistica, resi, commissioni e IVA definiti. Non chiamare costo per ordine «CAC» se include clienti già acquisiti.
- Livello di affidabilità: soglia di spend sufficiente, finestra di conversione, lag, stagionalità, inventario/prezzo, confidenza campionaria e dati incompleti. Prodotti senza vendita ma con spesa minima = «osservare», non «dannosi».
- Classificare SKU in: **spreco candidato** (spesa significativa, ritorno sotto soglia), **sostenibile**, **stella sottospinta** (ROAS/volume elevati, budget/visibilità limitati), **potenziale da testare** (domanda proxy Merchant/GSC ma no Shopping), **problema feed/prezzo**, **non valutabile**.
- **Soglie robuste (configurabili, mai inventate come verità)**: prima di classificare uno SKU come «spreco candidato» richiedere *tutte* queste condizioni, dichiarando i valori usati: (a) finestra di osservazione ≥ 30 giorni, oltre il lag di conversione dichiarato dall'account; (b) spesa SKU ≥ 2× il costo-per-ordine massimo sostenibile (prezzo medio × margine lordo dichiarato, oppure valore medio ordine / ROAS break-even); se margine/break-even non sono noti, usare solo l'etichetta «da osservare» e chiedere il dato; (c) un numero minimo di clic (default proposto: 100, modificabile dall'utente) per avere un tasso di conversione stimabile; (d) nessuna modifica rilevante a prezzo, stock, feed, titolo o bidding nella finestra (consultare `account-governance`/`merchant_history`); (e) confronto con la stagionalità/periodo precedente quando disponibile. Con dati sotto soglia: «non valutabile» o «osservare». Mostrare l'intervallo d'incertezza o dire che non è calcolabile; non usare un singolo valore puntuale come prova.
- Per ogni SKU candidato all'esclusione mostrare ID, titolo, campagna, spesa, clic, acquisti verificati, valore, ROAS, giorni osservati, confronto stagionale, break-even dichiarato, ragione specifica, impatto potenziale *stimato e incerto*. Non escludere automaticamente.
- Confrontare strategie: escludere un SKU, correggere feed, cambiare struttura, ridurre CPC, rivedere prezzo o stock, adeguare obiettivo ROAS. Simulare il caso prezzo solo con costo reale e tasso conversione come variabile: non assumere che riducendo prezzo le vendite aumentino automaticamente.

## Formula e avvertenze
`ROAS_purchase = SUM(valore purchase verificato attribuito) / SUM(spesa Ads)`; `CPO = SUM(spesa Ads) / COUNT(ordini attribuiti verificati)`. Se il denominatore è zero, indicare n.d., non 0/∞ nel report. ROAS lordo non è profitto. Un report Ads senza dati gestionali può stimare ordini attribuiti, non certificare tutte le vendite reali.

Output per prodotto + sintesi economica; specificare periodo, attribuzione, scope, valuta, qualità join e se il dataset è completo.
