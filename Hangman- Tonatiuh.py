import random
winning = False
ha_u_lose = False
guess_total = 8
db_info = False;
word_bank = ["Karen", "please", "give", "me", "back", "the", "kids", "I", "miss", "them"]
chosen_word = random.choice(word_bank)
chosen_word = chosen_word.lower()
chosen_word = chosen_word.upper()
list_word = list(chosen_word)
correct_guesses = []
letters_guessed = []
# Add * to list

for i in range(0, len(list_word)):
    correct_guesses.append("*")

while guess_total > 0 and winning == False:
    print("YOU HAVE %d something left" % guess_total)
    print(correct_guesses)

    letter = input("guess a letter ya wanker")
    letter = letter.lower()
    letter = letter.upper()
    letters_guessed.append(letter)

    for i in range(len(list_word)):
        if list_word[i] in letters_guessed:
            correct_guesses.pop(i)
            correct_guesses.insert(i, list_word[i])


    if letter not in list_word:
       guess_total -= 1

    if guess_total == 0:
        print(" oo oo aa aa heee hee hah ha yOuve Been GnoMed")
        ha_u_lose = True

    if correct_guesses == list_word:
        print("KEEMSTAR")
        winning = True