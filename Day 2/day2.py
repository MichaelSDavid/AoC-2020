from re import split
    
# Part 1
count = 0

with open('input.txt') as f:
    for line in f:
        mini, maxi, char, passwd = split('-| |: ', line)
        if int(mini) <= passwd.count(char) <= int(maxi):
            count += 1

print(f"Pass rule one:\n{count}")

# Part 2
count = 0

with open('input.txt') as f:
    for line in f:
        pos_a, pos_b, char, passwd = split('-| |: ', line)
        if (char == passwd[int(pos_a)-1]) ^ (char ==  passwd[int(pos_b)-1]):
            count += 1
        
print(f"Pass rule two:\n{count}")
