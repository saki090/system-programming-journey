import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)
print('Server waiting for connection...')
# accept incoming connection
conn, addr = server.accept()
print(f"Connected by {addr}")
# recieve data/message 
message = conn.recv(1024).decode()
print(f"Recieved meassage: {message}")
# send response back
conn.sendall("Message received! Go faster!".encode())

conn.close()
server.close()
