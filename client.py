import socket

# Create a client socket
cSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
cSocket.connect(("127.0.0.1",25))

# Send data to server
message = input("Please enter your message:")
cSocket.send(message.encode())

# Receive data from server
server_data = cSocket.recv(1024)

# Print to the console
print(server_data.decode())