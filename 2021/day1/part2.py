with open('input.txt') as input:
    raw_depths = [int(i) for i in input.readlines()]
depths = [raw_depths[i:i+3] for i in range(0, len(raw_depths))]
depth_increases = 0
for i in range(1, len(depths)):
    if sum(depths[i]) > sum(depths[i - 1]):
        depth_increases += 1 
print(f"{depth_increases} depth increases")