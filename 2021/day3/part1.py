with open("input.txt") as input:
    MEASUREMENTS = input.read().splitlines()  # drops \n from each line

INPUT_MEASUREMENT_COUNT = len(MEASUREMENTS)
DIGITS_PER_MEASUREMENT = len(MEASUREMENTS[0])


def get_final_rate(digits):
    return int(bin(int("".join(digits), 2)), 2)


def select_digits(digits, selector):
    # int(truthy value) returns 1 if truthy, 0 if falsy
    return [str(int(selector(d))) for d in digits]


# Since we're dealing with 0 and 1, we might be able to use addition to get the counts
# If there are more 1's than 0's, the sum of the column will be greater than the number
# of measurements / 2

digit_sums = [0] * DIGITS_PER_MEASUREMENT
for m in MEASUREMENTS:
    digit_sums = list(map(sum, zip(digit_sums, [int(d) for d in m])))

g = select_digits(digit_sums, lambda d: d >= (INPUT_MEASUREMENT_COUNT / 2))
e = select_digits(digit_sums, lambda d: d < (INPUT_MEASUREMENT_COUNT / 2))

gamma_rate = get_final_rate(g)
epsilon_rate = get_final_rate(e)

print(
    f"Power consumption is "
    f"{gamma_rate * epsilon_rate} "
    f"[{gamma_rate}g * {epsilon_rate}e]"
)
