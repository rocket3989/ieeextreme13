# Collin Pearce 17% TLE/memory limit
dp = {}
def isValid(string):
    if(len(string)) == 1: return True
    if string in dp:
        return dp[string]
    for i in range(len(string)):
        if string[:i] <= string[i:]:
            if isValid(string[:i]) and isValid(string[i:]):
                dp[string] = True
                return True
    dp[string] = False
    return False


for val in range(int(input())):
    if isValid(input()): print(1, end='')
    else:  print(0, end='')

# to check if a string is valid, divide it
# check if the first part is greater than the second, 
# then check if both halves are viable
# base case is a single letter, which is true