binary = input("Enter a 4-bit binary number: ")

if len(binary) == 4 and binary[0] != '0' and all(bit in "01" for bit in binary):
    data = []

    for i in range(4):
        data.append(int(binary[i]))

    hamming = [0, 0, data[0], 0, data[1], data[2], data[3]]
    parity_positions = [1, 2, 4]

    for p in parity_positions:

        parity = 0

        for i in range(1, 8):

            if i & p:
                parity = parity ^ hamming[i - 1]

        hamming[p - 1] = parity

    print("Hamming Code:", "".join(map(str, hamming)))

    received = input("Enter received Hamming Code: ")

    if len(received) == 7 and all(bit in "01" for bit in received):

        received = list(map(int, received))

        error = 0

        for p in parity_positions:

            parity = 0

            for i in range(1, 8):

                if i & p:
                    parity = parity ^ received[i - 1]

            if parity == 1:
                error = error + p

        if error == 0:

            print("No error detected")

        else:

            print("Error detected at position:", error)

            if received[error - 1] == 0:
                received[error - 1] = 1
            else:
                received[error - 1] = 0

            print("Corrected Hamming Code:",
                  "".join(map(str, received)))

            data = []

            for i in [2, 4, 5, 6]:
                data.append(received[i])

            print("Corrected Data:",
                  "".join(map(str, data)))

    else:
        print("Invalid Hamming Code")

else:
    print("Not valid")