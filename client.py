import socket

class client():


    def client(self):
        HOST = "127.0.1.1"
        PORT = 2906

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client.connect((HOST,PORT))
        message = input("\nEnter your message: ").encode("utf-8")
        client.send(message)


if __name__ == "__main__":

    while True:
        object = client()
        object.client()
        choice = input("Send another message? (Y/N)")
        if choice == "N":
            print("Goodbye")
            break