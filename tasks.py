
import os
from datetime import datetime
from .connection import netmiko_session

BACKUP_DIR = "./backups"

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def backup_running_config(device):
    ensure_dir(BACKUP_DIR)
    with netmiko_session(device) as conn:
        output = conn.send_command("show running-config")
    filename = f"{device['name']}_{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.cfg"
    file_path = os.path.join(BACKUP_DIR, filename)
    with open(file_path, 'w') as f:
        f.write(output)
    return file_path

def run_show_command(device, command):
    with netmiko_session(device) as conn:
        return conn.send_command(command)
