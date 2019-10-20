# Collin Pearce
# used to find GCD corner cases
from random import randint

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

N = randint(1, 10**3)
K = randint(1, N)

vals = []
gcds = {}
try:
    for i in range(N):
        num = randint(1, 10**4)
        vals.append(num)
        
        new = False
        if num not in gcds:
            gcds[num] = 1
            new = True
        if gcds[num] > 1 or new:
            gcds[num] = 1
            for key in list(gcds.keys()):
                newVal = gcd(key, num)
                if gcds[key] <= K:
                    gcds.setdefault(newVal, gcds[key] + 1)
                    if gcds[newVal] > gcds[key] + 1: gcds[newVal] = gcds[key] + 1
    print(len(gcds))
except:
    print(N, K, *vals)

