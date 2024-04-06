import json
import time
import _init_path as _init_path

from server_client.server_client import Client

with Client(port=7878) as client:
    if client.is_connected():
        data = client.recv_data()
        print(f'client recv: {data}')