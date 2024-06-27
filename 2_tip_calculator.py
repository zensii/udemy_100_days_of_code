bill = float(input('What is the bill: '))

tip = int(input('How much tip would you like to give: '))

number_of_ppl = int(input('How many people are you: '))
payment = bill * (1 + tip/100) / number_of_ppl

print(f'Each person should give {payment:.2f}')
