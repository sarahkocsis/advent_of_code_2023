#!/usr/bin/env python3
import re


def main():
    # Read in input
    input_path = "/Users/Sarah/Library/CloudStorage/OneDrive-Personal/Documents/Advent_of_Code_2023/Day1/input.txt"

    with open(input_path, 'r') as fil:
        inputs = [line.rstrip('\n') for line in fil]

    digit_list = [re.findall("\d", x) for x in inputs]

    chosen_digits = [int(x[0]+x[-1]) for x in digit_list]

    answer = sum(chosen_digits)

    print(answer)


if __name__ == "__main__":
    main()
