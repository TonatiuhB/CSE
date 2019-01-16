import random
import string
print(list(string.ascii_letters))
print(string.digits)
guesses_left = 0
guess = 10
word_bank = ["Karen"]
random.choice(word_bank)

for i in range(len(5)):
    print()