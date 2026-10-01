
import socket

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("localhost", 9999)

# Bind server to address and port
server_socket.bind(server_address)

print("UDP Server started...")
print("Server is waiting for client...")

while True:
    try:
        data, client_address = server_socket.recvfrom(1024)

        received_data = data.decode()

        # Check whether the message contains "|"
        if "|" not in received_data:
            result = "Invalid data format"
            server_socket.sendto(result.encode(), client_address)
            continue

        choice, message = received_data.split("|", 1)

        print("\nClient connected from:", client_address)
        print("Message received:", message)

        if choice == "1":
            result = message.lower()

        elif choice == "2":
            result = message.upper()

        elif choice == "3":
            result = message[::-1]

        else:
            result = "Invalid choice"

        # Send result back to client
        server_socket.sendto(result.encode(), client_address)

        print("Response sent:", result)

    except Exception as e:
        print("Server error:", e)