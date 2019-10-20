# Collin Pearce 10%
N, K, Q = [int(x) for x in input().split()]

arr = [int(x) for x in input().split()]

for q in range(Q):
    query = input().split()
    if query[0] == "Q":
        start, end = int(query[1]), int(query[2])

        arr1 = arr[start - 1:end]
        for i in range(K):
            for j in range(1, len(arr1)):
                arr1[j] += arr1[j-1] 
                arr1[j] %= 10**9 + 7
        print(arr1[-1])
    else:
        arr[int(query[1]) - 1] = int(query[2])
# naiive solution, just take repeated 