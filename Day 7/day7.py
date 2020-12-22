import re

# Part 1
with open('input.txt') as f:
    lines = f.read().splitlines()

bags = {}
count = 0

for line in lines:
    c = re.match(r"(.+?) bags contain", line)[1]  
    bags[c] = re.findall(r"(\d+?) (.+?) bags?", line)

def has_gold(c):
    if c == "shiny gold": 
        return True
    else:
        return any(has_gold(c) for _, c in bags[c] )

for bag in bags:
    if has_gold(bag):
        count += 1

print("AL shiny gold: " + str(count - 1))

# Part 2
def count_bags(btype):
    return 1 + sum(int(n)*count_bags(c) for n, c in bags[btype])

print("N individuals: " + str(count_bags("shiny gold")-1))
