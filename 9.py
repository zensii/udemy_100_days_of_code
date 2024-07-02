# silent bidding
import os


def add_participant(participants):
    name = input('What is your name: ')
    bid = input('What is your bid: ')
    participants[name] = int(bid)


print('Welcome to the silent auction.')
participants = {}

while True:
    add_participant(participants)
    more_ppl = input('Are there other participants, Yes or No? ')
    if more_ppl == 'No':
        print(f'The winner is {max(participants, key=participants.get)} with {max(participants.values())} USD.')
        break
    else:
        os.system('cls')
