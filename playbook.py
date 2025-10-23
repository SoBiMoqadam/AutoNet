
from jinja2 import Template
from .connection import netmiko_session

def render_template(template_path, variables):
    with open(template_path) as file:
        template = Template(file.read())
    return template.render(**variables)

def push_config(device, config_text):
    with netmiko_session(device) as conn:
        return conn.send_config_set(config_text.splitlines())
