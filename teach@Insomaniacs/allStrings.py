# What are Strings?
##
## Strings are sequence of characters. Strings can be used to display
## text on the display, showcasing data, manipulating data, and much
## more.
##
# **Topics Need to Cover:**
## String Is a Sequence, Traversal with a for Loop, String Slices,
## Strings Are Immutable, Searching, Looping and Counting, String Methods,
## The in Operator, String Comparison, String Operations.

## Let us start with absolute basics i.e how to declare a string?
## One of different things about string is that it needs to be
## surrounded with single quotes (' ') or double quotes (" ").
## This is done to represent the start and the end of the string.

a = "Hello, world"
b = "I like Python"
print(a)
print(a[4:]) # slice of a string.
a = "test"   # Strings are immutable i.e Cannot be modified.
print(a)
print(a.find("world")); # finding & string methods
print(b.find("test")); # finding & string methods

# The `in` Operator
if "test" in a:
    print("Test is present")
elif "world" in a:
    print("world is present")
else:
    print("test and world both are not found in the string");

if a>b:
    print("A is greater than B");
elif a<b:
    print("B is greater than A");
else:
    print("Both are Equal")

# String Operations:
c = a + b
print(c)
print(c*2)

# Traversing with for loop:
##
## When we use for loop with string, Python takes each character into
## iterable variable.
##
## Let us see a small example:
##

for x in a:
    print(x)


