import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6060))
s.listen(5)

try:
    while True:
        clientSocket, address = s.accept()
        print(f"Connection established from address: {address}") #kjo do te printoje ip dhe port

        try:
            while True:
                messageFromClient = clientSocket.recv(2048).decode("utf-8")
                print(f"Message from client: {messageFromClient}")

                if messageFromClient.lower() == "no":
                    print("Client requested to terminate the communication.")
                    break  

                response = input("Enter a response for the client: ")
                clientSocket.send(bytes(response, "utf-8"))
        
        except Exception as e:
            print(f"An error occurred while handling the client: {e}")
        finally:
            clientSocket.close()

except KeyboardInterrupt:
    print("\nServer terminated by the user.")
finally:
    s.close()

