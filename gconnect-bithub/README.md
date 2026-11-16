# GConnect by BitHub — plugin per Claude Code

Skill e connessione MCP a GConnect (`https://gconnect.able2code.com/mcp`) per analizzare in sola lettura Google Ads, Merchant Center, GA4 e Search Console del proprio e-commerce.

**Il plugin non contiene password, segreti o token e non dà accesso ai dati da solo**: serve un account BitHub con sottoscrizione GConnect attiva. Il server applica permessi e isolamento tra clienti.

## Installazione

```
/plugin marketplace add OWNER/gconnect-claude
/plugin install gconnect-bithub@bithub-plugins
```

Poi digitare `/mcp`, scegliere **gconnect** → **Authenticate** e accedere con le credenziali BitHub nel browser. Infine chiedere a Claude: «Verifica che GConnect funzioni e dimmi quali siti posso analizzare».

## Skill incluse
`setup`, `ads-onboarding`, `ads-audit`, `sku-economics`, `merchant-audit`, `ga4-audit`, `gsc-audit`, `account-governance`, `reports` (in Claude compaiono come `/gconnect-bithub:<nome>`).

## Problemi comuni
- *needs authentication*: ripetere `/mcp` → gconnect → Authenticate.
- *Nessun sito visibile / fonte disabilitata*: l'attivazione dei permessi è gestita da BitHub (https://bithub.it).
- Non scrivere mai password o codici in chat.
