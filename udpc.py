import socket

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("localhost", 9999)

print("UDP Client started...")

while True:
    print("\n1. Uppercase to Lowercase")
    print("2. Lowercase to Uppercase")
    print("3. Reverse String")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Validate choice
    if choice == "4":
        print("Client closed.")
        break

    if choice not in ("1", "2", "3"):
        print("Invalid choice. Please enter 1, 2, or 3.")
        continue

    message = input("Enter a string: ")

    # Combine choice and message
    data = choice + "|" + message

    try:
        # Send data to server
        client_socket.sendto(data.encode(), server_address)

        # Receive response
        response, server_address = client_socket.recvfrom(1024)

        print("Server response:", response.decode())

    except Exception as e:
        print("Client error:", e)
        break

    again = input("\nDo you want to continue? (yes/no): ")

    if again.lower() == "no":
        break

client_socket.close()

