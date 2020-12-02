from itertools import combinations

with open("input.txt", "r") as f:
    content = f.readlines()

# Part 1
group = combinations(content, 2)

for pair in group:
    if int(pair[0]) + int(pair[1]) == 2020:
        print(f"Pair:\n{int(pair[0]) * int(pair[1])}")

# Part 2
group = combinations(content, 3)

for triplet in group:
    if int(triplet[0]) + int(triplet[1]) + int(triplet[2]) == 2020:
        print(f"Triplet:\n{int(triplet[0]) * int(triplet[1]) * int(triplet[2])}")
