with open("input.txt") as input:
    movements = input.readlines()

location = [0, 0, 0]

for m in movements:
    match [x := m.split(), x[0], int(x[1])]:
        case [_, "forward", i]:
            location[0] += i
            location[1] += i * location[2]
        case [_, "down", i]:
            location[2] += i
        case [_, "up", i]:
            location[2] -= i

print(f"location is {location}. product is {location[0] * location[1]}")
