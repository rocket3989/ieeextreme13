# Collin Pearce 25% TLE
MOD = 10**9 + 7
from collections import deque
def bfs(node):
    total = 0
    todo = deque()
    todo.append((node, -1, 0))
    while(len(todo)):
        current = todo.popleft()
        for connected in adj[current[0]]:
            if connected[0] == current[1]: continue
            maxSeen = max(current[2], connected[1])
            total += maxSeen 
            total %= MOD
            todo.append((connected[0], current[0], maxSeen))
    return total

N = int(input())
adj = [[] for i in range(N)]
for i in range(N - 1):
    A, B, cost = [int(x) for x in input().split()]
    adj[A - 1].append((B - 1, cost))
    adj[B - 1].append((A - 1, cost))
count = 0
for i in range(N):
    count += bfs(i)
print((count // 2) % MOD)

# BFS from each point to every other node, keeping track of max edge seen
# every traversal, add max seen to total count
# add up all bfs, then div by 2, as each node pair was tested twice