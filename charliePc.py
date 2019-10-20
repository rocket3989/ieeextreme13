# Collin Pearce 12% TLE
dp = {}
components = []
lens = []

def solve(choice, money):
    if choice == -1: return money
    if (choice, money) in dp:
        return dp[(choice, money)]
    minRet = money

    for component in components[choice]:
        newMoney = money - component + components[choice][0]
        if newMoney >= 0:
            minRet = min(minRet, solve(choice - 1, newMoney))
    dp[(choice, money)] = minRet
    return minRet



for tc in range(int(input())):
    budget = int(input())
    N = int(input())
    components = []
    lens = []
    cost = 0
    input()
    for i in range(N):
        components.append(sorted([int(x) for x in input().split()]))
        cost += components[-1][0]
        lens.append(len(components[-1]))
    if cost > budget:
        print(0)
        continue
    
    index = [0 for i in range(N)]

    print(budget - solve(N - 1, budget - cost))
    
    
# create dp dict of choice, money. generate by quering possible monies and choice - 1
    