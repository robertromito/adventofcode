import math
import operator

o2_check = operator.ge
co2_check = operator.lt

with open("input.txt") as input:
    MEASUREMENTS = input.read().splitlines()  # drops \n from each line


INPUT_MEASUREMENT_COUNT = len(MEASUREMENTS)
DIGITS_PER_MEASUREMENT = len(MEASUREMENTS[0])


def get_final_rate(digits):
    return int(bin(int("".join(digits), 2)), 2)


def scan_measurements(measurements, comparison_func):
    measurement_count = len(measurements)
    compare_to = math.ceil(measurement_count / 2)
    sums = [0] * DIGITS_PER_MEASUREMENT
    for m in measurements:
        sums = list(map(sum, zip(sums, [int(d) for d in m])))
    final = [str(int(comparison_func(d, compare_to))) for d in sums]
    return final


def get_life_support_measurement(comparison_func):
    remaining_measurements = MEASUREMENTS
    for i in range(DIGITS_PER_MEASUREMENT):
        val = scan_measurements(remaining_measurements, comparison_func)
        remaining_measurements = [m for m in remaining_measurements if m[i] == val[i]]
        if len(remaining_measurements) == 1:
            break
    return remaining_measurements[0]


o2_generator_rate = get_final_rate(get_life_support_measurement(o2_check))
co2_scrubber_rate = get_final_rate(get_life_support_measurement(co2_check))

print(
    f"Life support rating is "
    f"{o2_generator_rate * co2_scrubber_rate} "
    f"[{o2_generator_rate}o2 * {co2_scrubber_rate}co2]"
)
