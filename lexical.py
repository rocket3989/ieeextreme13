# Collin Pearce 93%
# Iskandar Sobirov found many corner cases

from math import ceil
N, A, B = [int(x) for x in input().split()]

if A > N // 2 and B < N:
    print("NO")
else:
    valList = []
    val = 0
    bCount = N // B
    N %= B 

    if N == 0:
        print("YES")
        print(*[B for i in range(bCount)])
    elif N < A:
        if A == B: print("NO")
        else:
            x = ceil((A - N) / (B - A))
            bCount -= x
            if bCount < 0: print("NO")
            else:
                N += B * x
                aCount = N // A
                N = N % A
                print("YES")
                print(*[A for i in range(aCount - 1)], A + N, *[B for i in range(bCount)])
    else:
        print("YES")
        print(N, *[B for i in range(bCount)])
    
# first choose as many at the end of the range as possible
# then do casework with what is left to find other elements
