from collections import Counter

# get inputs from a text file
with open("input.txt") as f:
    lines = f.read().split("\n")

# map the inputs to a left and right list
left = []
right = []
for line in lines:
    x, y = map(int, line.split())
    left.append(x)
    right.append(y)

# Use a hashmap to keep count of number of times the number appears
hashmap = Counter(right)
score = 0
for dist in left:
     if dist in hashmap:
         score += dist * hashmap[dist]

print("Similarity Score:", score)