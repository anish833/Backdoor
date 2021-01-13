
import socket

Server_Address = input("Type the server IP address: ")
Server_Port = int(input("Type the server port: "))

def print_menu():
    print("""\n\n0) Close the connection
1) Get system info
2) List directory contents""")

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((Server_Address, Server_Port))

print("Connection established")
print_menu()

while 1:
    message = input("\n-Select an option: ")

    if(message == "0"):
        my_socket.sendall(message.encode())
        my_socket.close()
        break
        
    elif(message == "1"):
        my_socket.sendall(message.encode())
        data = my_socket.recv(1024)
        if not data: break
        print(data.decode('utf-8'))
        
    elif(message == "2"):
        path = input("Insert the path: ")
        my_socket.sendall(message.encode())
        my_socket.sendall(path.encode())
        data = my_socket.recv(1024)
        data = data.decode('utf-8').split(",")
        print("*"*40)
        for x in data:
            print(x)
        print("*"*40)
        
    print_menu()

