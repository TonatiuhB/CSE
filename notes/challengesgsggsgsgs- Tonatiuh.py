# 1
def challenge1(firstname, lastname):
   print(lastname, firstname)
challenge1("booga", "ooga")


# 2
def challenge2(number):
    if number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

challenge2(233333333333333333333333333334)


# 3


# 4
def challenge4(number):
    if number > 0:
        print("HAhahahahHAhah pOsitive")
    elif number < 0:
        print("haha neeegative")
    else:
        print("no it 0")
challenge4(-4)



# 7
def challenge7(number):
    print(number+number*number+number**3)

challenge7(2)


def pythagorean(a, b):
    return(a**2+b**2)**(1/2)

print(pythagorean(3, 4))

# 8
def challenge8(n):
    if n in range(150, 2000):
        print("issa between 150 and 2000")
    else:
        print("now it between 2000, 3000")
challenge8(2001)