import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# network
HOST = "127.0.1.1"
PORT = 2906

# binding yo server
def start_server():
    """
    This our main server function, used to start the server
    """
    # binding server
    server.bind((HOST,PORT))



def server_listening():

    # once the server is on we start to listen for oncoming connections
    server.listen()
    # 5 is the max number of unaccepted connections we want

    # accepting the clients request to connect
    com_socket, client_address = server.accept()

    # receiving the message, then decoding it
    message = com_socket.recv(1024).decode("utf-8")

    print(f"message from {client_address}: {message}")

    return com_socket, client_address, message


start_server()
while True:
    server_listening()