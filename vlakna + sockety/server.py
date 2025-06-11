# Inicializacia servera a cakanie na 2 hracov
import socket
import threading


class game_server:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []  # Zoznam hracov

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(2)
        print(f"Server bezi na {self.host}:{self.port},caka na 2 hracov.")

        while len(self.clients) < 2:
            client_socket, addr = self.server_socket.accept()
            print(f"Hrac sa pripojil z adresy {addr}")

            self.clients.append(client_socket)
            if len(self.clients) == 1:
                client_socket.sendall(b"WAITING\n")
            else:
                for client in self.clients:
                    client.sendall(b"START\n")

        print("Obaja hraci su pripojeny")
        # Tu sa spusti logika hry.


if __name__ == "__main__":
    server = game_server()
    server.start()