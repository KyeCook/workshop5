"""
Lottery Ticket Generator
Workshop 5
"""
import random


def main():
    quick_pick_amount = int(input("How many quick picks? :"))

    loop_iteration = 0
    while loop_iteration < quick_pick_amount:
        loop_iteration += 1
        lottery_lists = lottery_calculations()
        print(sorted(lottery_lists))


def lottery_calculations():
    lottery_list = []
    while len(lottery_list) < 6:
        number = random.randint(1, 45)
        if number not in lottery_list:
            lottery_list.append(number)
    return lottery_list
main()
