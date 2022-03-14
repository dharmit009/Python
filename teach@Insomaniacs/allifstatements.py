# What are `if` statements?

# 1. The If statements are conditional statements in python which are used to
# determine whether the given condition is `True` or `False`. Depending on
# the condition the program execute further statements.

# 2. Here is the basic syntax of an `IF` statement:

# * IF Statements:
#
# ```python
# if <condition>:
# <--identation--><statements>
# <--identation--><statements>
# <blank-line>
# ```
# Show other variations as well if-else, if-elif-else, and nested if
# possible and show basic working.

# 3. Show a couple of examples of the same:
#
# FOR EXAMPLE: Odd or even ...
n = int(input("Enter a number: "));
if n % 2==0:
    print(f"{n} is an even number.")
else:
    print(f"{n} is an odd number.")

if n==1:
    print(f"{n} is equal to one");
elif n==2:
    print(f"{n} is equal to two");
elif n==3:
    print(f"{n} is equal to three");
else:
    print(f"{n} is not equal to 1, 2, or 3");


if n<3:
    if n == 1:
        print(f"{n} is equal to one");
    else:
        print(f"{n} is equal to two");

elif n == 3:
    print(f"{n} is equal to three");

else:
    print(f"The Value of n is {n}");












