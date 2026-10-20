import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(5)

server_address = ("127.0.0.1", 9999)

print("UDP Client started...")

while True:
    print("\n1. Uppercase to Lowercase")
    print("2. Lowercase to Uppercase")
    print("3. Reverse String")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "4":
        break

    if choice not in ("1", "2", "3"):
        print("Invalid choice")
        continue

    message = input("Enter a string: ")
    data = choice + "|" + message

    try:
        client_socket.sendto(data.encode(), server_address)
        response, address = client_socket.recvfrom(1024)
        print("Server response:", response.decode())

    except socket.timeout:
        print("ERROR: Server did not respond. Check that udps.py is running.")

    again = input("Continue? (yes/no): ")
    if again.lower() == "no":
        break

client_socket.close()
