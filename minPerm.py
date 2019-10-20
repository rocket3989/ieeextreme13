# Collin Pearce 100%
input()
A = [int(x) for x in input().split()]
B = sorted([int(x) for x in input().split()])

posA, posB = 0,0

lenA = len(A)
lenB = len(B)

while True:
    if posA == lenA:
        print(*B[posB:])
        break
    if posB == lenB:
        print(*A[posA:])
        break
    if A[posA] < B[posB]:
        print(A[posA], end=' ')
        posA += 1
    else:
        print(B[posB], end=' ')
        posB += 1

# perform merge on A and sorted B