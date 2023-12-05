#!/usr/bin/env python3

def calc_card_score(winning_numbers, received_numbers):
    curr_score = 0
    curr_quantity_found = 0
    for num in received_numbers:
        if num in winning_numbers:
            curr_quantity_found = curr_quantity_found + 1
            curr_score = 2 ** (curr_quantity_found - 1)
    return curr_score, curr_quantity_found


def part1():
    """How many points are the cards worth in total?"""

    # Read in file into winning numbers and card numbers
    with open("input.txt", 'r') as cards_file:
        cards = cards_file.read().splitlines()

    cards_score = 0
    for card in cards:
        # Remove the Card # part
        card = card[10:]

        # Split on | to determine winning numbers and card numbers. There is exactly one | per line
        winning_nums_str, received_nums_str = card.split("|")
        curr_winning_nums = [int(x) for x in winning_nums_str.split()]
        curr_received_nums = [int(x) for x in received_nums_str.split()]

        # Calculate score of card
        cards_score += calc_card_score(curr_winning_nums, curr_received_nums)

    print(cards_score)


def part2():
    """How many total scratchcards do you end up with?"""

    # Read in file into winning numbers and card numbers
    with open("input.txt", 'r') as cards_file:
        cards = cards_file.read().splitlines()

    # card_copies = {}
    # card_copies[1] = 1  # The first card has one copy
    copies_count = 1
    cards_to_investigate = [1]

    while cards_to_investigate:
        # Sort to make sure cards are in ascending order
        cards_to_investigate = sorted(cards_to_investigate)
        curr_card_num = cards_to_investigate.pop(0)
        print(curr_card_num)
        # Remove the Card # part
        card = cards[curr_card_num][10:]

        # Split on | to determine winning numbers and card numbers. There is exactly one | per line
        winning_nums_str, received_nums_str = card.split("|")
        curr_winning_nums = [int(x) for x in winning_nums_str.split()]
        curr_received_nums = [int(x) for x in received_nums_str.split()]

        # Calculate number of matches on card
        _, num_matches = calc_card_score(curr_winning_nums, curr_received_nums)

        # Add the next n cards based on num_matches to the investigation list
        new_cards_to_add = list(range(curr_card_num+1,curr_card_num+1+num_matches))
        copies_count = copies_count + len(new_cards_to_add)
        cards_to_investigate = cards_to_investigate + new_cards_to_add

    print(copies_count)


if __name__ == "__main__":
    # part1()
    part2()
