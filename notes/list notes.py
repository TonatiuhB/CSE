# lists
shopping_list = [ "whole milk,", "PC", "Eggs", "trash", "other trash"]
print(shopping_list)
print(shopping_list[0])
print("the second thing in the lst is %s" % shopping_list[1])
print("the length of the list is %d" % len(shopping_list))

# changing elements in a list heeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeewwwwwwwwwwwwwwwwwwwwww
shopping_list[0]= "2% mILK"
print(shopping_list)
print(shopping_list[0])

# looping the list
for item in shopping_list:
    print(item)


new_list = ["egg", "ooga booga", "my dignity"]

new_list[2]= "liberals"
print(new_list)
print("the last thing in the list is %s" % new_list[len(new_list)-1])

# getting part of the list
print(new_list[1:3])
print(new_list[1:4])
print(new_list[1:])
print(new_list[:2])


# add to a list
holiday_list = []
holiday_list.append("taco")
holiday_list.append("bumbledee")
holiday_list.append("cowboy game")
print(holiday_list)
# notice this is object.method(parameters)

# remove stuff from a list
holiday_list.remove("taco")
print(holiday_list)

good_list = []
good_list.append("knack 2")
good_list.append("clay")
good_list.append("lorax limited edition dvd")
print(good_list)

good_list.append("ooga booga")
good_list.remove("clay")
print(good_list)

#also
holiday_list.pop(0)
print(holiday_list)

# Tuple
brands = ("apple", "sony", "samsungh")

colors = ["BLU", "yellow", "red", "black", "five", "magenta", "teal"]
print(len(colors))

# find the index
print(colors.index("teal"))

# changing things into a list
string1 = "yellow"
list1 = list(string1)
print(list1)
for character in list1:
    if character == "u":
        # replace with an a '
    current_index = list1.index(character)
    list1.pop(current_index)
    list1.insert(current_index, "*")

# changing lits into strings
print("ooga".join(list1))