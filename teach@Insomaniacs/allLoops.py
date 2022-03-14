# What are loops?

# Loops are used to repeate a block of code for number of times until
# the condition is met. If the condition is not met it is known as
# **Infinite Loop** as the loop will never end. Whereas if the
# condition is met then it breaks outside the loop and continues
# further.

# There are 2 loops in Python and they are as follows:
# 1. For Loop.
# 2. While Loop.

# The Syntax for `FOR LOOP` is as follows:
# for (condition):
# <--Identation--> <statements>
# <--Identation--> <statements>
# <blank-line>

# Another Variant for `FOR LOOP`:
# for x in <IterableObject>:
# <--Identation--> <statements>
# <--Identation--> <statements>
# <blank-line>

# WHILE LOOP:

# Infinite Loop:
# while True:
# <--Identation--> <statements>
# <--Identation--> <statements>
# <blank-line according to pep8 Instructions>

# Finite Loop:
# while <condition>:
# <--Identation--> <statements>
# <--Identation--> <statements>
# <blank-line according to pep8 Instructions>

for x in range(0,5):
    print("for x in range of 0 to 5: " ,x)

print("")
i = 0;
while i < 5:
    print("While I<5: ", i);
    i+=1;
