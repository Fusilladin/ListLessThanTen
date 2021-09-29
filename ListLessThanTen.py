a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b=[]
for element in a:
    if element < 5:
        b.append(element)
    else:
        print("\nThe current number list is:\n{}".format(b))
        break

while True:
    try:
        num = str(input("Pick a number 1-100  "))
        num_str = num.split(" ")[0]
        num_1 = int(float(num_str))
        if num_1 > 100:
            raise ValueError(print("Sorry that number is not between 1-100, try again."))
        if num_1 < 1:
            raise ValueError(print("Sorry that number is not between 1-100, try again."))
    except:
        continue
    else:
        print("Your number is {}".format(num_1))
        break

for element in a:
    if element < num_1:
        b.append(element)
    else:
        print("\nThe numbers from the list less than your number are:\n{}".format(b))
        break


# Take a list, say for example this one:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
#
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.

# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
