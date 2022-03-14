# TOPICS TO COVER:
# Tuples, Accessing values in Tuples, Tuple Assignment, Tuples as
# return values, Variable-length argument tuples, Basic tuples operations,
# Concatenation, Repetition, in Operator, Iteration, Built-in Tuple
# Functions.

# What are tuples?
## Tuples are kind a like list but with one exception and that is they
## are immutable which means you cannot modify the contents of a tuple.
##
## To declare a tuple we use round parathesis `()` a.k.a circular
## brackets.
##
## Tuple do not have methods like append, pop, or remove as it
## immutable.
##
## Let us see an example of tuple

a = (1, 1, 1, 8, 6);
b = ("test", "test2", 3)

print(f"A: {a}")
print("No of one's in tuple: ", a.count(1))
print("Find 6 and returns it index value:", a.index(6))
print("Return value of index[3]: ", a[3])

print("\nConcatenation: ");
c = a + b
print(f"A: {a}")
print(f"B: {b}")
print(f"C: {c}")


print("\nFor Loop with tuple: ")
for i, x in enumerate(c):
    print(f"c[{i}]:", x)
