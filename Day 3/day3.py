from functools import reduce

# Part 1
with open("input.txt") as f:
    grid = f.read().splitlines()

w_pattern = len(grid[0])
x = 0
count = 0

for line in grid:
    if line[(x % w_pattern)] == "#":
        count += 1
    x += 3

print("Count:", str(count))

# Part 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
results = []

for slope_num, slope in enumerate(slopes):
    count = 0
    x = 0
    x_int = slope[0]
    y_int = slope[1]

    for line in grid[::y_int]:
        if line[(x % w_pattern)] == "#":
            count += 1
        x += x_int

    results.append(count)

print(reduce((lambda a,b: a*b), results))
