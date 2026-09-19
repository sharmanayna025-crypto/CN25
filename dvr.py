INF = 999
n = 4
print("FLOYD-WARSHALL ALGORITHM")
print("\nEnter cost matrix (-1 for no connection):")
dist = []
for i in range(n):

    row = []
    for j in range(n):
        if i == j:
            row.append(0)
        else:
            x = int(input("Enter cost: "))
            if x == -1:
                row.append(INF)
            else:
                row.append(x)
    dist.append(row)

for k in range(n):

    for i in range(n):

        for j in range(n):

            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(n):

    print("          ROUTING TABLE FOR NODE", chr(65 + i))
    print("Destination\tDistance")
    print("----------------------------------")

    for j in range(n):

        if dist[i][j] == INF:
            print(chr(65 + j), "\t\tINF")
        else:
            print(chr(65 + j), "\t\t", dist[i][j])

    print("----------------------------------")

print("\nShortest distances between all pairs of nodes")
print("have been calculated successfully.")
