# print("Thank you for choosing Python Pizza Deliveries!")
# size = input() # What size pizza do you want? S, M, or L
# add_pepperoni = input() # Do you want pepperoni? Y or N
# extra_cheese = input() # Do you want extra cheese? Y or N
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
#
# sizes = {'S':15,'M':20,'L':25}
# peperoni = {'S':2,'M':3,'L':3}
# add_cheese = 1 if extra_cheese == 'Y' else 0
#
# bill = sizes[size] + peperoni[add_pepperoni] + add_cheese
#
# print(f'Your final bill is: ${bill}.')

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
first_digit = 0
second_digit = 0
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

for letter in 'true':
  if letter in name1.lower() or letter in name2.lower():
    first_digit += name1.count(letter)
    first_digit += name2.count(letter)

for letter in 'love':
  if letter in name1.lower() or letter in name2.lower():
    second_digit += name1.count(letter)
    second_digit += name2.count(letter)


final_score = int(str(first_digit)+str(second_digit))

if 10 > final_score < 90:
  print(f'Your score is {final_score}, you go together like coke and mentos.')
elif 40 < final_score < 50:
  print(f'Your score is {final_score}, you are alright together.')
else:
  print(f'Your score is {final_score}.')