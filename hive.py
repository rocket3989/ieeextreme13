# Collin Pearce 49% TLE
def test(hive, X, Y, offX, offY, N, M):
    Y += offY
    X += offX
    if X < N and X >= 0 and  Y >= 0 and Y < (M - ((X) % 2)):
        return hive[X][Y] == 1 
    return False

from collections import deque

N, M = [int(x) for x in input().split()]
hive =[[] for i in range(N)]
for i in range(N):
    hive[i] = [int(x) for x in input().split()]

for q in range(int(input())):
    query = input().split()
    if query[0] == 'a':
        hive[int(query[1]) - 1][int(query[2]) - 1] = 1
    else:
        bfs = deque()
        if hive[int(query[1]) - 1][int(query[2]) - 1] == 1:
            bfs.append((int(query[1]) - 1, int(query[2]) - 1))
        perimeter = 0
        visited = set()

        while len(bfs):
            current = bfs.popleft()
            if current in visited: continue
            visited.add(current)

            x, y = current

            if (test(hive, x, y, 1, 0, N, M)):
                bfs.append((x + 1, y))
            else:
                perimeter += 1

            if (test(hive, x, y, 0, 1, N, M)):
                bfs.append((x, y + 1))
            else:
                perimeter += 1
            
            if (test(hive, x, y, -1, 0, N, M)):
                bfs.append((x - 1, y))
            else:
                perimeter += 1

            if (test(hive, x, y, 0, -1, N, M)):
                bfs.append((x, y - 1))
            else:
                perimeter += 1

            if x % 2 == 1:
                if (test(hive, x, y, -1, 1, N, M)):
                    bfs.append((x - 1, y + 1))
                else:
                    perimeter += 1

                if (test(hive, x, y, 1, 1, N, M)):
                    bfs.append((x + 1, y + 1))
                else:
                    perimeter += 1
            else:
                if (test(hive, x, y, 1, -1, N, M)):
                    bfs.append((x + 1, y - 1))
                else:
                    perimeter += 1

                if (test(hive, x, y, -1, -1, N, M)):
                    bfs.append((x - 1, y - 1))
                else:
                    perimeter += 1
        print(perimeter)

# run modified hex bfs for each perimeter query, 
# +1 to perimiter if there, add the queue if not