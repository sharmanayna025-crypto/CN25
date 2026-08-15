def intro():
    print("\nDefinition of Subnetting:")
    print("Subnetting is the process of dividing a large network into")
    print("smaller networks called subnets. It helps to:")
    print("1. Reduce network congestion.")
    print("2. Improve network security.")

    print("\nDefinition of Subnet Mask:")
    print("A subnet mask is a 32-bit number used to separate the")
    print("network portion and the host portion of an IP address.")
    print("It tells which part of the IP address belongs to the")
    print("network and which part belongs to the hosts.\n")

    print("Every subnet contains:")
    print("- Network Address  : First address of the subnet.")
    print("- Host Addresses   : Addresses assigned to devices.")
    print("- Broadcast Address: Last address of the subnet used to")
    print("                     send data to all devices in the subnet.")


def check_class(num):

    if num >= 1 and num <= 126:

        print("IP Class            : Class A")
        print("Range               : 1 - 126")
        print("Default Subnet Mask : 255.0.0.0")
        print("Network Bits        : 8")
        print("Host Bits           : 24")
        print("Number of Hosts     : 2^24 - 2 = 16,777,214")

        print("\nWhy subtract 2?")
        print("Total possible host addresses = 2^24")
        print("- 1 address is reserved as the Network Address.")
        print("- 1 address is reserved as the Broadcast Address.")
        print("Therefore, usable hosts = 2^24 - 2.\n")

        print("Broadcast Address:")
        print("The last IP address of the network is called the")
        print("Broadcast Address. It is used to send data to every")
        print("device in the network.")

        print("\nNumber of networks: 2^7")
        print("Reason: This is because in Class A the starting bit is always 0")


    elif num == 127:

        print("It is Loopback Address range.")
        print("It is used for testing and troubleshooting the")
        print("local computer.")


    elif num >= 128 and num <= 191:

        print("IP Class            : Class B")
        print("Range               : 128 - 191")
        print("Default Subnet Mask : 255.255.0.0")
        print("Network Bits        : 16")
        print("Host Bits           : 16")
        print("Number of Hosts     : 2^16 - 2 = 65,534")

        print("\nWhy subtract 2?")
        print("Total possible host addresses = 2^16")
        print("- 1 Network Address")
        print("- 1 Broadcast Address")
        print("Therefore, usable hosts = 2^16 - 2.\n")

        print("Number of networks : 2^14")
        print("Reason: Class B has 16 network bits,")
        print("but the first 2 bits are fixed as 10.")
        print("Therefore, variable network bits = 16 - 2 = 14.")


    elif num >= 192 and num <= 223:

        print("IP Class            : Class C")
        print("Range               : 192 - 223")
        print("Default Subnet Mask : 255.255.255.0")
        print("Network Bits        : 24")
        print("Host Bits           : 8")
        print("Number of Hosts     : 2^8 - 2 = 254")

        print("\nWhy subtract 2?")
        print("Total possible host addresses = 2^8")
        print("- 1 Network Address")
        print("- 1 Broadcast Address")
        print("Therefore, usable hosts = 2^8 - 2.\n")

        print("Number of networks: 2^21")
        print("Reason: Class C has 24 network bits,")
        print("but the first 3 bits are fixed as 110.")
        print("Therefore, variable network bits = 24 - 3 = 21.")


    elif num >= 224 and num <= 239:

        print("IP Class : Class D")
        print("Range    : 224 - 239")
        print("Purpose  : Multicasting")
        print("These addresses are not assigned to individual hosts,")
        print("so host calculation is not applicable.")


    elif num >= 240 and num <= 255:

        print("IP Class : Class E")
        print("Range    : 240 - 255")
        print("Purpose  : Reserved for research and experimental use.")
        print("These addresses are not assigned to hosts.")


    else:

        print("Invalid IP Address.")

intro()

address = input("\nEnter an IPv4 Address: ")

parts = address.split(".")
number = int(parts[0])

print()

check_class(number)