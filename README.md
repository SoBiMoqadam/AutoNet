# NetBot 🛠️ — Python Network Automation Bot

**NetBot** is a compact, reliable Python tool for automating common network tasks on routers and switches.
It helps you backup device configs, run show commands across devices, and push Jinja2-based templates — fast.

![CLI demo](assets/cli_example.png)

## Quick Highlights
- SSH automation with **Netmiko**
- Multi-vendor support ideas with **NAPALM**
- Templating via **Jinja2**
- Simple CLI built with **Typer**
- YAML inventory for devices

## Quick Start
```bash
pip install -r requirements.txt
cp examples/devices.example.yml devices.yml
# edit devices.yml with your lab credentials (do NOT use production creds in GitHub)
python -m netbot.cli backup_all
python -m netbot.cli show sample-router "show ip interface brief"
```

## Security
**Do not** commit real device credentials. Keep `devices.yml` in `.gitignore` and use `examples/devices.example.yml` for public repos.

---
Powered by Netmiko, Jinja2 and Python. Fork it, improve it, automate your network. 🚀
