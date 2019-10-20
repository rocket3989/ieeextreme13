# Collin Pearce- 0pts TLE/memlimit

from math import log
dpFact = [-1 if i > 1 else 1 for i in range(10**5 + 1)]
for i in range(1, 10**4):
    dpFact[i] = (dpFact[i-1] * i)


def getCombinations(N, power, combinations):
    # if (N, power, combinations) in combDp:
    #     return combDp
    
    if (power == 0):
        combTotal = dpFact[sum(combinations)]
        for ele in combinations:
            combTotal = combTotal // dpFact[ele]
        return combTotal
    total = 0
    count = 0
    if power == 1:
        return getCombinations(0, power - 1, combinations + [N])
    while ((2 ** power) - 1) * count <= N:
        newComb = combinations[:] + [count]
        total += getCombinations(N - ((2 ** power) - 1) * count, power - 1, newComb)
        count += 1
    return total

for tc in range(int(input())):
    B = int(input())
    print((int(getCombinations(B, int(log(B + 1, 2)), [])) * 2) % (10**9 + 7))

# recurrence solution to find all combinations of paths, then find sum up combinations over them. not fast enough.