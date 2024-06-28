import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
askiart = {'rock':rock,'paper':paper,'scissors':scissors}

user_choice = input('Select rock, paper, or scissors: ')


print(f'You selected : {askiart[user_choice]}')
weapons = ['rock','paper','scissors']

logic = {'rock': 1, 'paper': 2, 'scissors': 3}
computer_choice = random.randint(1, 3)
print(f'computer selected: {askiart[next(weapon for weapon, value in logic.items() if value == computer_choice)]}')
if logic[user_choice] == computer_choice:
    print('draw')
else:
    if (logic[user_choice] > computer_choice and not computer_choice == 1) or (logic[user_choice] == 1 and computer_choice == 3):
        print('You WIN!')
    else:
        print('You LOSE!')


