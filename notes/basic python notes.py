'''
print("Hello world!")
# pointless comment
# hey hey hey
# it has no effect on the code
print() # this adds another space
print("This will print here. notice the printing")

a = 3
b = 4
print(a + b)
print(a + 5)
print(5-3)
print(6 / 5)


print("figure this out BuGGer")
print(6 % 4)
print(12 % 3)
print(9 % 4)

# variables
car_name = "heckers"
car_type = "Tesla"
car_cylinders = 1024
car_miles_per_gallon = 0.01

print("heheehhehehei have car")

name = input("what name is you")
print("Hello %s" % name)

# auto-comment - Ctrl + /
# age = input("how old are you? ")
# print("%s?! you belong in museum." % age)

# hidddden age
real_age = int(input("how old is ya? >_"))
hidden_age = real_age + 5
print(hidden_age)
print("%d is incredibly old." % (hidden_age, real_age))
'''

#fucntions
def printHelloWorld():
    print("Hello World!")


printHelloWorld()
'''
this is a multi-line comment
I can type anywhere here.
'''

# f(x) + 2x + 3
def f(x) :
    print(2*x + 3)
f(1)
f(5)
f(5000)

#loops
for i in (1, 2, 3):
    printHelloWorld()

print()
for i in range(100):
    printHelloWorld()

print()
for i in range(5):                                                                                                                                                          # range starts at 0 and goes to 4
    f(i)

for i in range(5):
    print(i**2)

# while loops
a = 0
while a < 10:
    print(a)
    a += 1 # this is the same things as a = a + 1

'''
hints with loops:
for loops - use when you know how exactly how many iterations
while loop - use when you dont know how many iterations

'''

# random numbers
import random # this should always be on line 1
print(random.randint(0, 100))

# control statement
def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

print(grade_calc(82))
