import socket

# operating on IPv4 addressing scheme
sSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# This is to bind and listen to the server
sSocket.bind(("127.0.0.1",25))
sSocket.listen()

# Accept connections
while(True):
    (cConnected, cAddress) = sSocket.accept()
    print("Accepted a connection request from %s:%s"%(cAddress[0], cAddress[1]))
    client_data = cConnected.recv(1024)
    print(client_data.decode())

    # Send the data back to the client
    cConnected.send("Hello Client:)".encode())

