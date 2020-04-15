# Marcos Duran 100%
n = int(input())
arr = ['0'] * (2*n)
x = 1
y = 2
pairsFound = 0
for i in range(n):
    print(x, y)
    line = input().split()
    if line[0] == "MATCH":
        arr[x-1] = arr[y-1] = '0' #pair found
        pairsFound+=1
    elif line[0] == '-1':
        sys.exit()
    else:
        arr[x-1] = line[0]
        arr[y-1] = line[1]
    x += 2
    y += 2
while pairsFound < n:
    for i in range(2*n):
        if arr[i] != '0':
            x = i
            for j in range(i+1, 2*n):
                if arr[j] == arr[i]:
                    y = j
                    print(x+1, y+1)
                    pairsFound+=1
                    arr[x] = arr[y] = '0'
                    break
            line = input()
print(-1)
