# Part 1
with open("input.txt") as f:
    content = f.read().strip().split('\n\n')

def ans(input, fcn):
    for group in content:
        yield len(fcn(*(set(s) for s in group)))

content = [line.split() for line in content]
print("Sum 1:", sum(ans(content, set.union)))

# Part 2
print("Sum 2:", sum(ans(content, set.intersection)))
