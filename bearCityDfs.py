# Collin Pearce 35% WA/TLE

from collections import deque

N, M = [int(x) for x in input().split()]

adj = [[] for i in range(M)]
edges = []

for i in range(M):
    A, B, cost = [int(x) for x in input().split()]
    adj[A - 1].append((B - 1, cost, i))
    adj[B - 1].append((A - 1, cost, i))
    edges.append((A - 1, B - 1, cost))

skip = [False for i in range(len(edges))]
for edgesList in adj:
    if len(edgesList) < 2:
        for edge in edgesList:
            skip[edge[2]] = True


ans = len(edges)
for i, edge in enumerate(edges):
    if skip[i]: continue

    A, B, cost = edge
    bfs = deque()
    bfs.append(A)
    visited = set()
    while len(bfs):
        val = bfs.popleft()
        if val in visited: continue
        visited.add(val)
        
        done = False
        for connect in adj[val]: 
            if connect[2] == i: continue
            if connect[1] > cost: continue
            if connect[0] == B: 
                ans -= 1
                done = True
                break
            bfs.append(connect[0])
        if done: break
       
print(ans)

# BFS of graph starting at one point of each edge
# if other point can be reached without traversing an edge longer than 
# examined edge, current edge is needed