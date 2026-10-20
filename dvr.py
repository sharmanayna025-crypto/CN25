INF = 999
n = int(input("enter no of nodes:"))

print("===== FLOYD-WARSHALL ALGORITHM =====")
print("Enter the 4x4 cost matrix row by row:")

dist = []

for i in range(n):
    row = list(map(int, input().split()))

    for j in range(n):
        if row[j] == -1:
            row[j] = INF

    dist.append(row)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(n):
    print("\nROUTING TABLE FOR NODE", chr(65 + i))
    print("Destination\tDistance")

    for j in range(n):
        if dist[i][j] == INF:
            print(chr(65 + j), "\t\tINF")
        else:
            print(chr(65 + j), "\t\t", dist[i][j])

print("\nShortest distances calculated successfully.")
