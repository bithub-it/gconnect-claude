---
name: gconnect-ecommerce-reports
description: Analizza dati di marketing, vendite e prestazioni e-commerce disponibili tramite GConnect, limitandoti ai clienti autorizzati.
---

# GConnect — Report e-commerce

> **Strumenti GConnect da preferire** (usa solo quelli presenti nell'elenco degli strumenti disponibili e rispetta i loro parametri): `client_overview` per un quadro d'insieme, poi gli strumenti specifici di ciascun audit. Se uno strumento manca o risponde «non autorizzato», dichiaralo e non aggirare il blocco.

Quando l'utente richiede analisi del proprio sito tramite GConnect:

- Individua il cliente autorizzato tramite `list_clients` e scopri le fonti tramite `list_sources`. Se ci sono più clienti, chiedi quale analizzare senza accedere a quelli non scelti.
- Usa soltanto strumenti e sorgenti effettivamente disponibili per quell'utente. Le fonti potrebbero includere Google Ads, GA4, Search Console, Merchant Center e servizi tecnici aggiuntivi.
- Distingui rigorosamente: conversioni Google Ads attribuite, acquisti GA4, ordini reali del gestionale (solo se una sorgente autorizzata li fornisce). Non assumere che coincidano o che GConnect conosca tutti gli ordini.
- Riporta date, fusi orari, valuta, periodo e limiti dei dati. Indica quando dati recenti sono parziali e possono essere aggiornati.
- Per confronti, preserva l'origine dei dati; non sommare visite Cloudflare e sessioni GA4, né unire identità prodotto senza una mappatura affidabile.
- I dati e-commerce di ogni cliente rimangono isolati. Non menzionare altre attività, segreti, identificativi OAuth, dati personali o chiavi API.
- Tutte le azioni restano in sola lettura. Se manca una fonte o il servizio restituisce un errore, spiega esattamente cosa manca e come chiedere l'attivazione a BitHub.

Formato predefinito: sintesi esecutiva con 3-5 osservazioni concrete, numeri con date e 1-3 azioni suggerite, senza inventare dati.

## Campagne Google Ads: rispetto delle preferenze
Se Google Ads è collegato, la prima valutazione dell'account richiede il profilo preferenze ottenuto dalla skill `gconnect-ads-onboarding`. Eseguire subito `gconnect-google-ads-audit` per campagne, obiettivi di bidding, canali e asset. Distinguere sempre acquisti reali, azioni di conversione, `Conversions` e `All conversions`. Segnalare con evidenze le reti YouTube/Display/partner attive contro le preferenze del cliente, ma non definirle automaticamente fraudolente o in perdita.

## Errori, permessi e dati parziali (comportamento obbligatorio)
- **Altro cliente / `client_id` non autorizzato**, fonte disabilitata o permesso negato dal server: riportare l'errore, dire che l'accesso è gestito dalla sottoscrizione BitHub e indicare di contattare BitHub. Non riprovare con altri identificativi, non enumerare clienti, non usare altre fonti per aggirare il blocco.
- **Token scaduto / autenticazione richiesta**: non chiedere credenziali in chat; invitare a ripetere l'autenticazione dal client (in Claude Code `/mcp` → gconnect → Authenticate; in ChatGPT riconnettere GConnect).
- **Risorsa o query non supportata dal catalogo** (es. GAQL/MCQL fuori elenco, `price_insights`/`price_competitiveness`/bestseller senza idoneità o autorizzazione): dichiarare «non disponibile/non autorizzato», non simulare il dato e non cercare scorciatoie; indicare la lacuna (vedi `MCP_GAPS.md`).
- **Dataset parziale o troncato** (paginazione incompleta, limiti di righe, dati recenti non consolidati): dichiarare copertura e campione; niente totali o classifiche come se fossero esaustivi.
- **Storico oltre i limiti** (es. `change_event` oltre 30 giorni, `change_status` oltre 90): dichiarare il limite della fonte; non ricostruire eventi mancanti.

## Moduli di audit per negozi online
Applicare in modo mirato: `merchant-audit`, `ga4-audit`, `gsc-audit`, `sku-economics`, `account-governance`. Per ogni opportunità servono evidenza, impatto plausibile e limiti; non etichettare prodotti «dannosi» prima di controllare spesa sufficiente, finestra attribuzione e margine dichiarato.
