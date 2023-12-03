#!/usr/bin/env python3

import re


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


if __name__ == "__main__":
    part1()
