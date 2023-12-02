#!/usr/bin/env python3
"""
Advent of Code Day 2 Star 2

What is sum of the power of the minimum number of cubes that must have been present per game?
"""


import re


def main():
    games_file = "games.txt"
    sum_powers = 0
    with open(games_file, 'r') as fil:
        games = [line.rstrip('\n') for line in fil]

    for game in games:
        # The maximum number of green cubes is the minimum number that were required to play that game
        green_list = re.findall(r"(\d+) green", game)
        max_green = max([int(x) for x in green_list])

        blue_list = re.findall(r"(\d+) blue", game)
        max_blue = max([int(x) for x in blue_list])

        red_list = re.findall(r"(\d+) red", game)
        max_red = max([int(x) for x in red_list])

        cube_power = max_green * max_blue * max_red
        sum_powers += cube_power

    print(sum_powers)


if __name__ == "__main__":
    main()
