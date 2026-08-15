import math

ip = input("Enter base IP address (e.g., 192.168.10.0): ")
o1, o2, o3, o4 = map(int, ip.split("."))

cidr = int(input("Enter CIDR prefix (e.g., 26 for /26): "))

if cidr < 24 or cidr > 30:
    print("Error: This program currently supports Class C subnetting (CIDR 24 to 30).")

else:

    hostBits = 32 - cidr
    blockSize = 2 ** hostBits
    numSubnets = 256 // blockSize
    usableHosts = blockSize - 2
    lastOctetMask = 256 - blockSize

    print("\n--- General Subnet Information ---")
    print("Calculated Subnet Mask : 255.255.255.", lastOctetMask)
    print("Total Usable Hosts     :", usableHosts, "per subnet")
    print("Total Subnets Created  :", numSubnets)
    print()

    for i in range(numSubnets):

        network = i * blockSize
        firstHost = network + 1
        lastHost = network + usableHosts
        broadcast = network + blockSize - 1

        print("=========================================")
        print("Subnet", i + 1)
        print("=========================================")

        print("Network Address   :", o1, ".", o2, ".", o3, ".", network, sep="")
        print("First Host        :", o1, ".", o2, ".", o3, ".", firstHost, sep="")
        print("Last Host         :", o1, ".", o2, ".", o3, ".", lastHost, sep="")
        print("Broadcast Address :", o1, ".", o2, ".", o3, ".", broadcast, sep="")

        print("\nUsable IP Addresses:")

        for j in range(firstHost, lastHost + 1):
            print("  ", o1, ".", o2, ".", o3, ".", j, sep="")

        print()