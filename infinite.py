# Collin Pearce 100%
# Marcos Duran found B==1 corner case

for tc in range(int(input())):

    B, X = [int(x) for x in input().split()]
    if B == 1: 
        print('a')
        continue
    count = 1
    segLen = 0
    segTotal = 0
    while X >= segTotal:
        segLen = (B ** count) * count
        segTotal += segLen
        count += 1
    count -= 1
    X -= (segTotal - segLen)

    pos = X % count
    pos = count - pos
    baseRep = X // count
    basePower = baseRep // (B ** (pos - 1))
    print(chr((basePower % B) + 97))

# breaks down the number to find which sequence it is in, eg x, xx, xxxxx
# finds the position in that sequence, then finds the char at that pos