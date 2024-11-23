import socket

def udp_server():
    try:
        # Create a UDP socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_port = 65432

        # Bind the socket to the address and port
        server_socket.bind(('127.0.0.1', server_port))
        print(f"Server is listening on port {server_port}...")

        # Receive data from client
        receive_buffer, client_address = server_socket.recvfrom(1024)
        client_message = receive_buffer.decode()
        print(f"Received from client ({client_address}): {client_message}")

        # Send a response back to the client
        response = f"Server received: {client_message}"
        server_socket.sendto(response.encode(), client_address)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the server socket
        server_socket.close()

# Run the server
if __name__ == "__main__":
    udp_server()
