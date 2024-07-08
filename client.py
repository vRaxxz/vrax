import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.100.22', 65432))  # Replace '192.168.100.22' with the actual IP address of the server
    
    welcome_message = client_socket.recv(1024)
    print(welcome_message.decode('utf-8'))
    
    while True:
        message = input("Enter message to send: ")
        client_socket.send(bytes(message, "utf-8"))
        response = client_socket.recv(1024)
        print(f"Response: {response.decode('utf-8')}")
        
        if message.lower() == "exit":
            break
    
    client_socket.close()

if __name__ == "__main__":
    start_client()
