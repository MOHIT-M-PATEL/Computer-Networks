import socket

def tcp_server():
    try:
        # Create a server socket and bind it to port 65432
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('127.0.0.1', 65432))
        server_socket.listen(1)
        print("Server listening on port 65432...")

        # Accept a connection from the client
        client_socket, client_address = server_socket.accept()
        print(f"Connected to client: {client_address}")

        # Receive message from the client
        client_message = client_socket.recv(1024).decode('utf-8')
        print(f"Received from client: {client_message}")

        # Send response back to the client
        response = f"Server received: {client_message}"
        client_socket.sendall(response.encode('utf-8'))

        # Close the connection
        client_socket.close()
        server_socket.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    tcp_server()
