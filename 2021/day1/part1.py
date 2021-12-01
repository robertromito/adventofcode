with open('input.txt') as input:
    depths = [int(i) for i in input.readlines()]
depth_increases = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i - 1]:
        depth_increases += 1 
print(f"{depth_increases} depth increases")