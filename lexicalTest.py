
from random import randint
from math import ceil
count = 0
while True:
    count += 1
    if count % 100 == 0: print(count // 100)

    N = randint(1, 10**5)
    B = randint(1, 10**5)
    A = randint(1, B)
    print(N, A, B)

    if (A > N // 2 and B < N) or N < A:
        continue
    else:
        A1 = A
        B1 = B
        N1 = N

        bCount = N // B
        N %= B 
        ans1 = []
        if N == 0:
            ans1 = [B for i in range(bCount)]
        elif N < A:
            if A == B: break
            else:
                print(N)
                x = ceil((A - N) / (B - A))
                print(x)
                bCount -= x
                N += B * x
                aCount = N // A
                print(aCount)
                N = N % A
                print(N)
                ans1 = [A for i in range(aCount - 1)] +  [A + N] +  [B for i in range(bCount)]
        else:
            ans1 = [N] + [B for i in range(bCount)]
        
        #   68166 306 307
        # A = A1
        # B = B1
        # N = N1


        # bCount = N // B

        # N %= B

        # ans2 = []
        # if N == 0:
        #     ans2 = [B for i in range(bCount)]
        # else:
        #     aCount = 0
        #     found = False
        #     if N >= A and N <= B:
        #         ans2 = [N] +  [B for i in range(bCount)]
        #         found = True
        #     while not found:
        #         N += B
        #         bCount -= 1
        #         while A <= N:
        #             N -= A
        #             aCount += 1
        #             if N >= A and N <= B:
        #                 ans2 = [A for i in range(aCount - 1)] +  [N] +  [B for i in range(bCount)]
        #                 found = True
        # if len(ans2) != len(ans1): print(N1, A1, B1)

        # for x, y in zip(ans1, ans2):
        #     if x != y: print(N1, A1, B1)

            