import socket

def udp_client():
    try:
        # Create a UDP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Define server address and port
        server_address = '127.0.0.1'
        server_port = 65432

        # Message to be sent to the server
        message = "Hello, Server!"
        client_socket.sendto(message.encode(), (server_address, server_port))
        print(f"Sent to server: {message}")

        # Receive response from the server
        receive_buffer, server = client_socket.recvfrom(1024)
        server_response = receive_buffer.decode()
        print(f"Received from server: {server_response}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the client socket
        client_socket.close()

# Run the client
if __name__ == "__main__":
    udp_client()
