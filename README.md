# GConnect — marketplace Claude Code di BitHub

Marketplace con il plugin **gconnect-bithub** (audit e-commerce in sola lettura su Google Ads, Merchant Center, GA4, Search Console tramite GConnect).

## Per i clienti

```
/plugin marketplace add OWNER/gconnect-claude
/plugin install gconnect-bithub@bithub-plugins
```

Poi `/mcp` → **gconnect** → **Authenticate** (login BitHub nel browser). Serve una sottoscrizione GConnect attiva: l'installazione da sola non dà accesso ai dati. Dettagli: [gconnect-bithub/README.md](gconnect-bithub/README.md).

## Per BitHub

- Struttura: `.claude-plugin/marketplace.json` (catalogo) + `gconnect-bithub/` (plugin: `.claude-plugin/plugin.json`, `.mcp.json`, `skills/`).
- Controllo prima di ogni rilascio: `claude plugin validate --strict .` e `python3 -I tools/check_repo.py`.
- Rilasciare un aggiornamento: aumentare `version` in `plugin.json` **e** in `marketplace.json`, aggiornare `CHANGELOG.md`, commit e push. I clienti aggiornano con `/plugin marketplace update` .
- Per attivare il plugin già selezionato per un team, nel `.claude/settings.json` del loro progetto: `extraKnownMarketplaces` (fonte GitHub `OWNER/gconnect-claude`) e `enabledPlugins` con `"gconnect-bithub@bithub-plugins": true`.
- Il repository è pubblico di proposito: contiene solo skill e URL del server. I dati sono protetti da OAuth e permessi sul server, non dalla segretezza del plugin. Non committare mai segreti.
