#!/usr/bin/env python3

import re

# 12 red cubes, 13 green cubes, and 14 blue cubes
RED_IN_BAG = 12
GREEN_IN_BAG = 13
BLUE_IN_BAG = 14


def main():
    games_file = "games.txt"
    sum_game_ids = 0
    with open(games_file, 'r') as fil:
        games = [line.rstrip('\n') for line in fil]

    for game in games:
        green_list = re.findall(r"(\d+) green", game)
        max_green = max([int(x) for x in green_list])

        blue_list = re.findall(r"(\d+) blue", game)
        max_blue = max([int(x) for x in blue_list])

        red_list = re.findall(r"(\d+) red", game)
        max_red = max([int(x) for x in red_list])

        if max_red <= RED_IN_BAG and max_blue <= BLUE_IN_BAG and max_green <= GREEN_IN_BAG:
            game_id = int(re.match(r"Game (\d+)", game).group(1))
            sum_game_ids += game_id


if __name__ == "__main__":
    main()
