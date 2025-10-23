
# NetBot - Network Automation Bot

## 📌 Overview
NetBot is a Python-based automation tool designed to manage network devices such as routers and switches. 
It uses SSH-based automation to collect configurations, push templates, and execute show commands across multiple devices.  
This project is modular, scalable, and perfect for network engineers who want to automate repetitive tasks.

## ✅ Features
- Connect to network devices using SSH (Netmiko)
- Backup running-configuration from devices
- Execute show commands on multiple devices
- Push configuration using Jinja2 templates
- Supports YAML-based device inventory
- Thread-based parallel execution

## 📂 Project Structure
```
netbot/
├─ netbot/                # Core Python source code
│  ├─ connection.py       # Handles SSH connections using Netmiko
│  ├─ tasks.py            # Backup and show command execution
│  ├─ playbook.py         # Jinja2 templating and config push
│  └─ __init__.py
├─ templates/             # Configuration templates (Jinja2)
│  └─ add_vlan.j2
├─ examples/              # Sample files (safe for GitHub)
│  └─ devices.example.yml
├─ requirements.txt
├─ .gitignore
├─ README.md
└─ LICENSE (optional)
```

## 🚀 How to Run
```bash
pip install -r requirements.txt
python -m netbot.cli
```

## ⚠️ Security Note
Do NOT upload real device credentials to GitHub.  
Use `devices.example.yml` instead of `devices.yml`, and add the real one to `.gitignore`.

## ⭐ Future Improvements
- REST API (FastAPI)
- Web dashboard
- Config versioning and diff
- Scheduled backups

