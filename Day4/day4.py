#!/usr/bin/env python3


def part1():
    """How many points are the cards worth in total?"""

    # Read in file into winning numbers and card numbers
    with open("input.txt", 'r') as cards_file:
        cards = cards_file.read().splitlines()

    # winning_nums = {}
    # received_nums = {}

    cards_score = 0

    card_num = 1
    for card in cards:
        # Remove the Card # part
        card = card[10:]

        # Split on | to determine winning numbers and card numbers. There is exactly one | per line
        winning_nums_str, received_nums_str = card.split("|")
        curr_winning_nums = [int(x) for x in winning_nums_str.split()]
        curr_received_nums = [int(x) for x in received_nums_str.split()]

        # # Add to dictionaries with card num
        # winning_nums[card_num] = curr_winning_nums
        # received_nums[card_num] = curr_received_nums

        # Calculate score of card
        curr_score = 0
        curr_quantity_found = 0
        for num in curr_received_nums:
            if num in curr_winning_nums:
                curr_quantity_found = curr_quantity_found + 1
                curr_score = 2 ** (curr_quantity_found - 1)
        cards_score = cards_score + curr_score
        card_num += 1

    print(cards_score)


if __name__ == "__main__":
    part1()
