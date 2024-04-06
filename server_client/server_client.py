import socket
import copy

class Base:
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        if self.connected:
            self.close()

    def __init__(self, host='127.0.0.1', port=9876) -> None:
        self.host = host
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False

    def close(self):
        self.connected = False
        self.s.close()

    def __del__(self):
        self.close()

    def _send(self, sk, data):
        sk.sendall(data)

    def _recv(self, sk, bufsize=1024):
        recv_data = b''
        while 1:
            rec = sk.recv(bufsize)
            if not rec:
                break
            recv_data += rec
            if len(rec) < bufsize:
                break
        return recv_data


class Client(Base):
    def __init__(self, host='127.0.0.1', port=9876) -> None:
        super().__init__(host, port)
        self.conn = None
        self.addr = None
        self.__connect()

    def __connect(self):
        self.s.bind((self.host, self.port))
        self.s.listen()
        self.conn, self.addr = self.s.accept()  # 接受连接
        self.connected = True
        print(f'connecting to: {self.addr[0]}:{self.addr[1]}')

    def __send(self, data):
        return super()._send(self.conn, data)
    
    def __recv(self, bufsize=1024):
        return super()._recv(self.conn, bufsize)
    
    def send_data(self, data, encoding='utf-8'):
        data = copy.deepcopy(data)
        if not isinstance(data, bytes):
            data = data.encode(encoding)
        self.__send(data)

    def recv_data(self, bufsize=1024, to_str=False):
        if to_str:
            return self.__recv(bufsize).decode()
        return self.__recv(bufsize)
    
    def is_connected(self):
        return self.connected
    
    def close(self):
        super().close()
        if self.conn: self.conn.close()

    def __del__(self):
        self.close()
        super().__del__()


class Server(Base):
    def __init__(self, host='127.0.0.1', port=9876, loop=False, max_times=5) -> None:
        super().__init__(host, port)
        self.loop = loop
        self.max_times = max_times
        self.__connect()

    def __del__(self):
        super().__del__()

    def __connect(self):
        t = 0
        while True and t < self.max_times:
            try:
                self.s.connect((self.host, self.port))
                print(f'connecting to {self.host}:{self.port}')
                self.connected = True
            except Exception as e:
                print(f'error: {e}')
                t += 1
            finally:
                if not self.loop or self.connected: 
                    break
    
    def __send(self, data):
        return super()._send(self.s, data)
    
    def __recv(self, bufsize=1024):
        return super()._recv(self.s, bufsize)

    def send_data(self, data, encoding='utf-8'):
        if not isinstance(data, bytes):
            self.__send(data.encode(encoding))
        else:
            self.__send(data)

    def recv_data(self, bufsize=1024, to_str=False):
        if to_str:
            return self.__recv(bufsize).decode()
        return self.__recv(bufsize)

    def is_connected(self):
        return self.connected
    
