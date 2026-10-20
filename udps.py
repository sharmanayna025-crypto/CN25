import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("127.0.0.1", 9999))

print("UDP Server is running on port 9999...")

while True:
    data, address = server.recvfrom(1024)
    print("Received:", data.decode())

    choice, message = data.decode().split("|", 1)

    if choice == "1":
        result = message.lower()
    elif choice == "2":
        result = message.upper()
    elif choice == "3":
        result = message[::-1]
    else:
        result = "Invalid choice"

    server.sendto(result.encode(), address)
    print("Sent:", result)
