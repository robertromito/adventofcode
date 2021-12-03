gamma_rate = 0  # most common bits in column
epsilon_rate = 0  # opposite of gamma_rate

with open("input.txt") as input:
    measurements = input.read().splitlines()  # drops \n from each line

# Since we're dealing with 0 and 1, we might be able to use addition to get the counts
# If there are more 1's than 0's, the sum of the column will be greater than the number
# of measurements / 2

number_of_measurements = len(measurements)
number_of_digits = len(measurements[0])
sums = [0] * number_of_digits
for m in measurements:
    sums = list(map(sum, zip(sums, [int(d) for d in m])))
g = [str(int(d >= (number_of_measurements/2))) for d in sums]
e = [str(int(d < (number_of_measurements/2))) for d in sums]
gamma_rate = int(bin(int("".join(g), 2)), 2)
epsilon_rate = int(bin(int("".join(e), 2)), 2)


print(f"Power consumption is {gamma_rate * epsilon_rate} [{gamma_rate}g * {epsilon_rate}e]")
