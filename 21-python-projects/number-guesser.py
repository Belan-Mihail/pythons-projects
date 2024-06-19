import random

# not include 11 
# r = random.randrange(-5, 11)
# print(r)

# include 11
# r1 = random.randint(-5, 11)
# print(r1)

top_of_range = input('Type a number: ')

# return True if all symbol in string are numbers
if top_of_range.isdigit():
    # int convert string to number
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time')
        quit()
else:
    print('Please type a number next time')
    quit()

random_number = random.randrange(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time')
        continue
    
    
    if user_guess == random_number:
        print('You got it!')
        break
    elif user_guess > random_number:
        print('You were above the number...')
    else:
        print('You were below the number...')

print('You got it in', guesses, 'guesses')

# 39:49