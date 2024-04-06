import _init_path as _init_path

from server_client.server_client import Server

with Server(port=7878, loop=True) as server:
    if server.is_connected():
        with open('ocr1.png', 'rb') as f:
            print('server send data...')
            server.send_data(f.read())

