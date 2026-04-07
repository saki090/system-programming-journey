import socket 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))
client.sendall("Hello, Server!".encode())
response = client.recv(1024).decode()
print(f"Server said: {response}")
client.close()