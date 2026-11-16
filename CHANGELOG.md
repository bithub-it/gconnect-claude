# Changelog
## 0.4.2
- Autenticazione con client Keycloak pubblico pre-registrato `gconnect-claude` (PKCE) e porta di callback fissa 8765: la registrazione dinamica del client non è disponibile sul server (HTTP 404).

## 0.4.2 (repository marketplace)
- Repository `gconnect-claude` strutturato come marketplace Claude Code: `.claude-plugin/marketplace.json` alla radice e plugin in `gconnect-bithub/`.
- Documentazione pubblica per clienti e BitHub; note interne (gap MCP, audit OAuth, test, kit ChatGPT) tenute fuori dal repository (`internal/`, ignorata da Git).
- Aggiunto `tools/check_repo.py`; `claude plugin validate --strict` senza warning o advice.
- Stato: NON PUBBLICATO. Installazione da marketplace NON ESEGUITA (nessun login nella config isolata di test).

## 0.4.1 (verifica e consegna, 2026-11-16)
- Claude Code: `claude plugin validate --strict` senza warning; plugin caricato in Claude Code 2.1.301 (9 skill, MCP in `needs-auth`).
- Marketplace: aggiunti description/metadata/categoria/versione; README con installazione in 3 passaggi e opzioni di distribuzione (nessuna pubblicazione effettuata).
- Skill `setup` Claude riscritta (flusso `/mcp` → Authenticate, niente riferimenti a ChatGPT). Skill ChatGPT `setup` e metadati ChatGPT invariati.
- Skill condivise (copie ChatGPT/Claude allineate): confronto target ROAS vs ROAS reale in `ads-audit`; soglie robuste per SKU in `sku-economics`; strategia di offerta tra le domande di `ads-onboarding`; sezione errori/permessi/dati parziali in `reports`.
- Aggiunti: `MCP_GAPS.md`, `OAUTH_FINDINGS.md`, `TEST_STATUS.md`, `tools/check_kit.py`, `test-reports/`.
- Non verificati (NON ESEGUITI): elenco reale dei tool, test autenticati e negativi, ChatGPT, installazione da marketplace.

## 0.4.0
- Plugin nativo Claude Code con manifest e MCP remoto (scaffold da validare nel client).
- Aggiunte skill Merchant, GA4, GSC, analisi economica SKU Shopping e governance account 30/90 giorni.
- Onboarding e-commerce orientato a Shopping, obiettivi validi, strategia bidding e canali non desiderati.
- Istruzioni in `CLAUDE.md` per validazione, distribuzione e gap analysis MCP.
- Mantenute skill precedenti, OAuth audit e impostazioni di sola lettura.
