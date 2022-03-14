# **Topic Need To Cover:**
# Values and Accessing Elements, Lists are mutable, traversing a List,
# Deleting elements from List, Built-in List Operators, Concatenation,
# Repetition, In Operator, Built-in List functions and methods

# What are lists?
##
## List are used to store collection of data. One of the biggest
## advantage of python list compare to array of many other language is
## that it allows to store different type of data within it's list.

print("For Loop with list: ")
a = [ 2, "Python", "haha", 34]
for i, x in enumerate(a):
    print(f"a[{i}]:", x)
print("")

# How to declare and initialize a list in Python?
##
## To declare a list we normally use the `list()` function which will
## provide us an empty list by default then we can initialize the value for
## the same. Another way is to use square brackets to declare and
## initialize a list. Here are the syntax for the both of them:

# Method 1:
b = list()
b = ["test1", "test2", "test3"]
# Method 2:
b = ["test1", "test2", "test3"]

# List are mutable
##
## It means that list can be modified. You can add, remove, or even
## modify the data entered within the list.
## Let us see an example:

a [0] = "Golang"

# List inbuilt functions.
print(f"Before: ")
print(f"A: {a}")
a.pop()
a.append("Java")
a.remove("haha")
a.reverse()
print(f"After: ")
print(f"A: {a}")

print("\nConcatenation: ");
c = a + b
print(f"A: {a}")
print(f"B: {b}")
print(f"C: {c}")

