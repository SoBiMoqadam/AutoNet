
from netmiko import ConnectHandler
from napalm import get_network_driver
import contextlib

@contextlib.contextmanager
def netmiko_session(device):
    conn = None
    try:
        conn = ConnectHandler(
            device_type=device['platform'],
            host=device['host'],
            username=device['username'],
            password=device['password']
        )
        yield conn
    finally:
        if conn:
            conn.disconnect()

def napalm_connection(device):
    driver = get_network_driver(device['platform'].split('_')[1])
    device_conn = driver(device['host'], device['username'], device['password'])
    return device_conn
