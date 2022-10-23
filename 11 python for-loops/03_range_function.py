# The range() Function

#! To loop through a set of code a specified number of times, we can use the range() function,
#! The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

for x in range(6):
    print(x)

print("-----------------------")
#! The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

for y in range(0,6):
    print(y)

print("-----------------------")
#! The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

for z in range(1,10,2):
    print(z)