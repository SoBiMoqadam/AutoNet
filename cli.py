
import typer
import yaml
from .tasks import backup_running_config, run_show_command

app = typer.Typer()

def load_devices():
    with open("devices.yml") as f:
        return yaml.safe_load(f)['devices']

@app.command()
def backup_all():
    devices = load_devices()
    for device in devices:
        path = backup_running_config(device)
        typer.echo(f"Backed up: {path}")

@app.command()
def show(device_name: str, command: str):
    devices = load_devices()
    for device in devices:
        if device['name'] == device_name:
            output = run_show_command(device, command)
            typer.echo(output)
            return
    typer.echo("Device not found")

if __name__ == "__main__":
    app()
