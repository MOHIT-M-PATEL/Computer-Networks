import socket

def tcp_client():
    try:
        # Create a client socket and connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 65432))

        # Send message to the server
        message = "Hello, Server!"
        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent to server: {message}")

        # Receive response from the server
        server_response = client_socket.recv(1024).decode('utf-8')
        print(f"Received from server: {server_response}")

        # Close the connection
        client_socket.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    tcp_client()
