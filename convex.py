# Collin Pearce 0% WA

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + ',' + str(self.y)
    def __repr__(self):
        return str(self.x) + ',' + str(self.y)


def ccw(A,B,C):
    return (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x)

def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def sub(A, B):
    return point(A.x - B.x, A.y - B.y) 

def dot(A, B):
    return A.x * B.x + A.y * B.y


N, M = [int(x) for x in input().split()]

polygon = []
for i in range(N):
    x, y = [int(x) for x in input().split()]
    polygon.append(point(x, y))

insideCount = 0

outside = []

for i in range(M):
    x, y = [int(x) for x in input().split()]
    for p0, p1 in zip(polygon, polygon[1:] + [polygon[0]]):
        if (y - p0.y) * (p1.x - p0.x) - (x - p0.x) * (p1.y - p0.y) < 0: 
            outside.append(point(x, y))
            break
    else: 
        insideCount += 1
        
outsideCount = 0

for i, p0 in enumerate(outside):
    for p1 in outside[i + 1:]:
        E = 0
        L = 1
        seg = sub(p1, p0)

        for v0, v1 in zip(polygon, polygon[1:] + [polygon[0]]):
            if intersect(p0, p1, v0, v1): 
                break
        else:
            outsideCount +=1


            # ev = sub()
            # n = (ev[1], -ev[0])
            # N = - ( (p0[0] - x0) * n[0] + (p0[1] - y0) * n[1])
            # D = seg[0] * n[0] + seg[1] * n[1]
            # if D == 0:
            #     if N < 0:
            #         outsideCount += 1
            #         break
            #     else: continue
            # t = N / D
            # if D < 0:
            #     E = max(t, E)
            #     if E > L:
            #         outsideCount += 1
            #         break
            # else:
            #     L = min(t, L)
            #     if L < E:
            #         outsideCount += 1
            #         break
print(outsideCount + (insideCount * (insideCount - 1)) // 2)

# problem haunted me entire tournament

# first classify each point as inside or outside polygon
# then draw a line between each outside point to every other
# if they don't intersect add to count
# all inside points can be connected