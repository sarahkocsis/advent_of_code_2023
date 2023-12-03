#!/usr/bin/env python3

import re
import math

def part1():

    with open("input.txt", "r") as day3:
        lines = day3.read().split("\n")

    schematic = []
    y = 0
    x = 0
    total = 0

    for line in lines:
        schematic.append([*line])

    for line in lines:
        data = re.finditer(r'(\d+)', line)
        for match in data:
            x=match.span()[0]
            while x<match.span()[1]:
                print(y, x)
                if schematic[y][x].isdigit():
                    if 0<=x-1<len(schematic[y]) and 0<=y-1<len(schematic[y]) and not schematic[y-1][x-1].isalnum() and schematic[y-1][x-1] != ".":
                        total += int(match.group())
                        break
                    elif 0<=x<len(schematic[y]) and 0<=y-1<len(schematic[y]) and not schematic[y-1][x].isalnum() and schematic[y-1][x] != ".":
                        total += int(match.group())
                        break
                    elif 0<=x+1<len(schematic[y]) and 0<=y-1<len(schematic[y]) and not schematic[y-1][x+1].isalnum() and schematic[y-1][x+1] != ".":
                        total += int(match.group())
                        break
                    elif 0<=x-1<len(schematic[y]) and 0<=y<len(schematic[y]) and not schematic[y][x-1].isalnum() and schematic[y][x-1] != ".":
                        total += int(match.group())
                        break
                    elif 0<=x+1<len(schematic[y]) and 0<=y<len(schematic[y]) and not schematic[y][x+1].isalnum() and schematic[y][x+1] != ".":
                        total += int(match.group())
                        break
                    elif 0<=x-1<len(schematic[y]) and 0<=y+1<len(schematic[y]) and not schematic[y+1][x-1].isalnum() and schematic[y+1][x-1] != ".":
                        total += int(match.group())
                        break
                    elif 0<=x<len(schematic[y]) and 0<=y+1<len(schematic[y]) and not schematic[y+1][x].isalnum() and schematic[y+1][x] != ".":
                        total += int(match.group())
                        break
                    elif 0<=x+1<len(schematic[y]) and 0<=y+1<len(schematic[y]) and not schematic[y+1][x+1].isalnum() and schematic[y+1][x+1] != ".":
                        total += int(match.group())
                        break
                    else:
                        x+=1
                else:
                    x += 1
        y += 1

    print(total)


def find_line_matches(x, line):
    number_matches = re.finditer(r"(\d+)", line)
    line_matches = []

    # Compute the x values that would count as a "touch"
    valid_touching_points = [x]
    if x > 0:
        valid_touching_points.append(x-1)
    if x < len(line):
        valid_touching_points.append(x+1)

    for match in number_matches:
        for val in valid_touching_points:
            if val in range(match.span()[0], match.span()[1]):
                line_matches.append(int(match.group()))
                break

    return line_matches


def find_numbers_around_star(x,y, schematic):

    numbers_list = []
    max_idx = len(schematic)  # same for both x and y
    min_idx = 0
    # Find numbers that touch the gear in the line above the current one
    if y >= min_idx:
        line_above = schematic[:][y-1]
        line_matches = find_line_matches(x, line_above)
        # If number touches, add to gears list
        if line_matches:
            numbers_list = numbers_list + line_matches
    # Find numbers that touch the gear in the line below the current one
    if y <= max_idx:
        line_below = schematic[:][y+1]
        line_matches = find_line_matches(x, line_below)
        # If number touches, add to gears list
        if line_matches:
            numbers_list = numbers_list + line_matches

    current_line = schematic[:][y]
    # Find all numbers
    line_matches = find_line_matches(x, current_line)
    # If number touches, add to gears list
    if line_matches:
        numbers_list = numbers_list + line_matches

    return numbers_list


def calc_gear_ratio(match, y, schematic):
    x = match.span()[0]  # For * will always be of size 1

    # A gear is an * that is adjacent to exactly two numbers
    numbers_list = find_numbers_around_star(x, y, schematic)
    if len(numbers_list) == 2:
        # Calculate gear ratio
        return math.prod(numbers_list)
    else:
        return 0


def part2():
    """What is the sum of all of the gear ratios in your engine schematic?"""
    # Read in input
    with open("input.txt", 'r') as schematic_file:
        schematic = schematic_file.read().splitlines()

    total = 0
    y = 0  # y coordinate of schematic

    # For each line, look for gears (*)
    for line in schematic:
        data = re.finditer(r'(\*)', line)
        for match in data:

            # Calc gear ratio. Will be 0 if * is not a gear
            gear_ratio = calc_gear_ratio(match, y, schematic)

            # Add gear ratio to total
            total += gear_ratio

        y += 1

    print(total)


if __name__ == "__main__":
    # part1()
    part2()
