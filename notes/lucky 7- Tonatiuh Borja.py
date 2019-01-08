import random

min = 1
max = 6

money = 15
roundS = 0
maxmonee = 15
goodround = 0

while money > 0:

    print("OkAy communist the values are....")
    dice1 = (random.randint(min, max))
    dice2 = (random.randint(min, max))
    print(dice1 + dice2)

    money -= 1
    roundS += 1

    if dice1 + dice2 == 7:
        print("good job comrade! ya got a 7!")
        money += 5
        if maxmonee < money:
            maxmonee = money
            goodround = roundS


    elif dice1 + dice2 != 7:
        print("ya lost one money ya socialist")
print(roundS)
print(maxmonee)
print(goodround)
