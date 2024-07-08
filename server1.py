import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 65432))
    server_socket.listen(5)
    print("Server is listening...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} has been established.")
        
        client_socket.send(bytes("Welcome to the server!", "utf-8"))
        
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode('utf-8')}")
            client_socket.send(data)  # Echo back the received data
        
        client_socket.close()

if __name__ == "__main__":
    start_server()
