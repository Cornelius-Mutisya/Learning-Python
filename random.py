import random
secretNumber = random.randint(1,20)
print('I am currently thinking of a number.')

for i in range(1,4):
    print('Try to guess the number')
    guess = int(input('Enter a number between 1 and 20: '))

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

if guess == secretNumber:
    print('Congrats. You guessed the number')
else:
    print('Better luck next time. The correct number was ' + str(secretNumber))
