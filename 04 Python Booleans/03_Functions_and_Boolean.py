
def myFunction():
    return True

if myFunction():
    print("Yes!")
else:
    print("No!")


print("--------------------------------")

#! Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

x = 200
print(isinstance(x, int))