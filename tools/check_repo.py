#!/usr/bin/env python3
"""Controlli statici del marketplace: JSON, percorsi, frontmatter skill, riferimenti relativi, assenza di segreti.
Uso: python3 -I tools/check_repo.py (dalla radice del repo)."""
import json, re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
fails = []
def chk(c, m): print("PASS" if c else "FAIL", m); (None if c else fails.append(m))
mk = json.loads((root/".claude-plugin/marketplace.json").read_text())
chk(mk.get("name") == "bithub-plugins", "marketplace name = bithub-plugins")
for pl in mk["plugins"]:
    d = (root/pl["source"]).resolve()
    chk(d.is_dir() and root in d.parents, f"source esistente dentro il repo: {pl['source']}")
    pj = json.loads((d/".claude-plugin/plugin.json").read_text())
    chk(pj["name"] == pl["name"], f"nome plugin coerente: {pl['name']}")
    chk(pj["version"] == pl.get("version"), f"versione plugin = marketplace ({pj['version']})")
    mcp = json.loads((d/".mcp.json").read_text())["mcpServers"]["gconnect"]
    chk(mcp["url"] == "https://gconnect.able2code.com/mcp" and mcp["type"] == "http", ".mcp.json: URL e tipo http corretti")
    skills = sorted(p.parent.name for p in (d/"skills").glob("*/SKILL.md"))
    chk(len(skills) == 9, f"9 skill presenti: {skills}")
    for n in skills:
        t = (d/"skills"/n/"SKILL.md").read_text()
        chk(re.match(r"---\nname: \S+\ndescription: .+\n---\n", t) is not None, f"frontmatter: {n}")
        chk("ChatGPT" not in t or n == "reports", f"niente riferimenti ChatGPT fuori contesto: {n}")
        for ref in set(re.findall(r"\.\./([a-z0-9-]+)/SKILL\.md", t)):
            chk((d/"skills"/ref/"SKILL.md").exists(), f"riferimento {n} -> ../{ref}")
sec = re.compile(r"(client_secret|password\s*[:=]|Bearer\s+[A-Za-z0-9._-]{20,}|eyJ[A-Za-z0-9_-]{20,}|api[_-]?key\s*[:=])", re.I)
hits = [str(f.relative_to(root)) for f in root.rglob("*") if f.is_file() and "internal" not in f.parts and ".git" not in f.parts and f.suffix in {".json",".md",".py"} and f.name != "check_repo.py" and sec.search(f.read_text(errors="ignore"))]
chk(not hits, f"nessun segreto evidente ({hits})")
print("\nRISULTATO:", "OK" if not fails else f"{len(fails)} FALLITI"); sys.exit(1 if fails else 0)
