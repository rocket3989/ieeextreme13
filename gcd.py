# Collin Pearce 55% TLE
gcdDp = {}
def gcd(a, b):
    A, B = a, b
    if (a, b) in gcdDp:
        return gcdDp[(a, b)]
    while b > 0:
        if (a, b) in gcdDp:
            gcdDp[(A, B)] = gcdDp[(a, b)]
            return gcdDp[(a, b)] 
        a %= b
        if a == 0:
            gcdDp[(A, B)] = b
            return b
        b %= a
    gcdDp[(A, B)] = a
    return a

N, K = [int(x) for x in input().split()]

gcds = {}

for num in [int(x) for x in input().split()]:
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

# create a gcds dict. Add new values to dict with values of '1' go through other k/v in dict
# if other value + 1 <= K, and this is less than what is stored at gcd(num, otherkey) store there
# output length of gcd