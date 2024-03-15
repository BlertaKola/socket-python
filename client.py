

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 6060))

try:
    while True:
        sendToServer = input("Enter a message to send to the server: ")

        s.send(bytes(sendToServer, "utf-8"))

        if sendToServer.lower() == "no":
            print("Terminating the communication.")
            time.sleep(1) 
            break 
        message = s.recv(2048).decode("utf-8")
        print(f"Message received from server: {message}")

except KeyboardInterrupt:
    print("\nClient terminated by the user.")
finally:
    s.close()
