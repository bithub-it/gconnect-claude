---
name: gconnect-setup
description: Aiuta un cliente BitHub a collegare e verificare GConnect in Claude (Claude Code), senza credenziali in chat e senza configurare manualmente URL MCP. Usala alla prima connessione o quando gli strumenti GConnect non risultano disponibili.
---

# GConnect — Attivazione per i clienti BitHub (Claude)

Scopo: ridurre il più possibile i passaggi necessari al nuovo cliente. Il server MCP `gconnect` è già dichiarato dal plugin: l'utente non deve inserire alcun URL.

1. Controlla se gli strumenti del server GConnect (`whoami`, `list_clients`, `list_sources`; in Claude Code compaiono come `mcp__plugin_gconnect-bithub_gconnect__…`) sono disponibili e rispondono. Non asserire che la connessione funzioni soltanto perché il plugin risulta installato.
2. Se il server risulta «needs authentication» o gli strumenti non rispondono, invita l'utente a digitare **`/mcp`**, selezionare il server **gconnect** e scegliere **Authenticate**: si apre il browser sulla pagina di accesso sicura BitHub, dove inserisce le credenziali fornite da BitHub. Non richiedere né ripetere username, password, token o codici OTP nella conversazione.
3. Se l'OAuth richiede conferma/autorizzazione, lascia che sia l'utente ad approvare nel flusso del proprio account. Se il browser non si apre, l'utente può copiare l'URL mostrato da `/mcp`; non chiedere mai di incollare in chat codici o token.
4. Quando la connessione è pronta, usa nell'ordine gli strumenti **whoami**, **list_clients**, **list_sources** (o gli equivalenti effettivamente disponibili) per confermare identità autorizzata, clienti visibili e fonti abilitate.
5. Mostra in italiano l'elenco dei siti che quell'utente può vedere e le sorgenti collegate. Non mostrare né cercare clienti fuori autorizzazione.
6. Proponi una sola prova immediata pertinente, come "mostrami le campagne degli ultimi 7 giorni" o "riassumi traffico e ordini"; eseguila soltanto quando l'utente la richiede.
7. Se non ci sono siti visibili o una fonte è disabilitata, spiega che l'attivazione dei permessi (sottoscrizione) è gestita da BitHub e va richiesta a BitHub: non tentare altri account, fonti o scorciatoie.
8. Se la sessione di accesso scade, indica di ripetere **`/mcp` → gconnect → Authenticate** (o «Re-authenticate»). Non tentare di aggirare l'autenticazione.

GConnect è un servizio commerciale BitHub con attivazione dei clienti e dei permessi gestita esternamente: **non promettere accesso gratuito o automatico a dati non autorizzati**. Non eseguire scritture o modifiche. Non dire "connessione riuscita" senza risposta positiva di uno strumento.

## Onboarding Google Ads obbligatorio, se presente
Dopo `list_sources`, se Google Ads è connesso e non risultano preferenze pubblicitarie già confermate, attiva `gconnect-ads-onboarding` (`../ads-onboarding/SKILL.md`). Chiedi tipologia di attività, obiettivi desiderati e indesiderati, canali/posizionamenti graditi o esclusi, strategia di offerta e cosa conta come conversione utile. Solo dopo le risposte esegui l'audit `gconnect-google-ads-audit` (`../ads-audit/SKILL.md`). Non affermare di conservare preferenze fra chat senza supporto storage verificato; se esistono, confermale senza ripetere inutilmente le domande.

## Check-up e-commerce alla prima connessione
Per negozi online con fonti abilitate eseguire o proporre subito audit Shopping per SKU, Merchant, GA4, GSC e cronologia Ads, con limiti espliciti. Se l'utente ha autorizzato più sorgenti, incrociarle solo mediante identificatori di prodotto e periodi verificati. Evitare questionari lunghi: iniziare da tipo sito, obiettivi desiderati/indesiderati e strategia bidding, poi analizzare.
