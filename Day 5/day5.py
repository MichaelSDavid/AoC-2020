# Part 1
seats = [
			int(
				(l.replace('B','1').replace('F','0')
				.replace('R','1').replace('L','0'))
				,2
			)
			for l in open('input.txt')
		]

print(f"Max seat: {max(seats)}")

# Part 2
seat = [s for s in range(min(seats), max(seats)) 
       if s not in seats][0]
print(f"Given seat: {seat}")
