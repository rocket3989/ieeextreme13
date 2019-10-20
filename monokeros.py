# Collin Pearce 75% TLE
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

input()

vals = [int(x) for x in input().split()]

root = Node(vals[0])
output = []
print(1, end=' ')
for val in vals[1:]:
    currNode = root
    depth = 1
    while True:
        depth += 1
        if val > currNode.val:
            if currNode.right == None:
                currNode.right = Node(val)
                print(depth, end=' ')
                break
            currNode = currNode.right
        else:
            if currNode.left == None:
                currNode.left = Node(val)
                print(depth, end=' ')
                break
            currNode = currNode.left
print()

# build a binary tree with given values, tracking depth
# when item is placed, output depth and move to next item