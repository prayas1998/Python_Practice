thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#! Negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#! Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#! Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")