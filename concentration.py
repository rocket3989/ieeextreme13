# Marcos Duran 100%
import sys

n = int(input())

guessX = 1
guessY = 2
indeces = []
cards = [0] * (2*n)
matchCount = 0

for i in range(n):
   
    # code below builds pairs of cards
    print(str(guessX) + ' ' + str(guessY), flush = True)
    valIn = input()
   #indeces = [int(x) for x in input().split()]
   
    if "MATCH" == valIn:
        #cards.insert(guessX-1, 0) # delete from deck
        #cards.insert(guessY-1, 0)
        guessX += 2
        guessY += 2
        matchCount += 1
    elif valIn != "-1":
        indeces = [int(x) for x in valIn.split()]
        currX = guessX-1
        currY = guessY-1
        cards.insert(currX, indeces[0])
        cards.insert(currY, indeces[1])
        guessX += 2
        guessY += 2
    else: # if receive -1, quit immeadiately
        sys.exit()
   
    #code below correctly solves all pairs
for i in range(0, 2*n):
    if matchCount == n:break
    if(cards[i] != 0):
        for j in range(i + 1, 2*n):
            if cards[j] == cards[i]:
                print(i + 1, j + 1, flush = True)
       
                input()
                cards[i] = 0
                cards[j] = 0
                matchCount += 1
                break
       
       
print("-1", flush = True)
