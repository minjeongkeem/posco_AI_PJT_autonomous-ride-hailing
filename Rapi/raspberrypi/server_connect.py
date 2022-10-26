# connect to server
# 2018.10.03
# BCODE

import socket

class Connect(object):
    def __init__(self, HOST, PORT):
        self.host = HOST
        self.port = PORT
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 클라이언트는 바인드 과정이 없으며, 그 자신이 접속을 능동적으로 수행하기 떄문에
        # 생성->연결->쓰기->읽기의 싸이클이 적용된다.
        self.server_socket.connect((self.host, self.port))
        print('Connected')

    def Get_Data(self):
        return self.server_socket.recv(2).decode()
    
    def Get_Socket(self):
        return self.server_socket

    def Send_Data(self, data) :
        self.server_socket.send(data)

    def __del__(self):
        self.server_socket.close()
           

