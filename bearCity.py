# Collin Pearce
from heapq import *

N, M = [int(x) for x in input().split()]

adj = [[] for i in range(M)]

for i in range(M):
    A, B, cost = [int(x) for x in input().split()]
    adj[A - 1].append((B - 1, cost))
    adj[B - 1].append((A - 1, cost))

connected = set()
connected.add(0)
edges = []

for edge, cost in adj[0]:
    heappush(edges, (cost, edge))

mstCost = 0

while (len(edges)):
    val = heappop(edges)
    if val[1] in connected: continue
    connected.add(val[1])
    mstCost += val[0]
    
    for edge, cost in adj[val[1]]:
        if edge not in connected:
            heappush(edges, (cost, edge))
print(mstCost)

# first try at bearCity, started off by finding the MST cast, then move to 
# generate all ST and find intersection of edges used? did not use