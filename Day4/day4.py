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
        current_score, _ = calc_card_score(curr_winning_nums, curr_received_nums)
        cards_score += current_score

    print(cards_score)


def part2():
    """How many total scratchcards do you end up with?"""

    # Read in file into winning numbers and card numbers
    with open("input.txt", 'r') as cards_file:
        cards = cards_file.read().splitlines()

    card_copies = {}
    # All cards have one copy to start
    for i in range(1, len(cards)+1):
        card_copies[i] = 1

    curr_card_num = 1

    for card in cards:
        # Remove the Card # part (length depends on input)
        card = card[10:]

        # Split on | to determine winning numbers and card numbers. There is exactly one | per line
        winning_nums_str, received_nums_str = card.split("|")
        curr_winning_nums = [int(x) for x in winning_nums_str.split()]
        curr_received_nums = [int(x) for x in received_nums_str.split()]

        # Calculate number of matches on card
        _, num_matches = calc_card_score(curr_winning_nums, curr_received_nums)

        # Add copies to the copies dictionary
        for _ in range(card_copies[curr_card_num]):
            for i in range(curr_card_num + 1, curr_card_num + num_matches + 1):
                card_copies[i] += 1

        curr_card_num += 1

    total = sum(card_copies.values())
    print(total)


if __name__ == "__main__":
    part1()
    part2()
