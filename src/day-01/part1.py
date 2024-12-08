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

# sort the left and right lists
left.sort()
right.sort()

# iterate through both lists and calulcate the difference
total_dist = sum(abs(x - y) for x, y in zip(left, right))

print("Total distance:", total_dist)