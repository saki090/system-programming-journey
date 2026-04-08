import socket
import threading

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    message = conn.recv(1024).decode()
    print(f"Received message {addr}: {message}")
    conn.sendall(f"Hello from threaded server!".encode())
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen(5)
print(5)
print("Threaded server running on localhost:9999...")

while True:
    conn, addr = server.accept()
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()
    print(f"Active connections: {threading.active_count() }")