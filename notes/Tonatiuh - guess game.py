import random

guessesTaken = 0

number = random.randint(1,10)

while guessesTaken < 5:
    print('ooga booga guess from 1 to 10.')
    guess = int(input())

    guessesTaken += 1

    if guess < number:
        print('too low communist.')

    elif guess > number:
        print('Too high liberal .')


    if guess == number:
        print('good job bugger')

if guess != number:
    number = str(number)
    print('Nope. The number was ' + number)