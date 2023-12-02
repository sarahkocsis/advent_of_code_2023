#!/usr/bin/env python3
import re


def main():
    # Read in input
    input_path = "/Users/Sarah/Library/CloudStorage/OneDrive-Personal/Documents/Advent_of_Code_2023/Day1/input.txt"

    with open(input_path, 'r') as fil:
        inputs = [line.rstrip('\n') for line in fil]

    corrected_data = []

    for x in inputs:
        # Compensate for edge cases
        x = x.replace("twone", "21")
        x = x.replace("oneight", "18")
        x = x.replace("eightwo", "82")

        # Standard replacement after edge cases
        x = x.replace("one", "1")
        x = x.replace("two", "2")
        x = x.replace("three", "3")
        x = x.replace("four", "4")
        x = x.replace("five", "5")
        x = x.replace("six", "6")
        x = x.replace("seven", "7")
        x = x.replace("eight", "8")
        x = x.replace("nine", "9")

        corrected_data.append(x)

    digit_list = [re.findall("\d", x) for x in corrected_data]

    chosen_digits = [int(x[0]+x[-1]) for x in digit_list]

    answer = sum(chosen_digits)

    print(answer)


if __name__ == "__main__":
    main()
