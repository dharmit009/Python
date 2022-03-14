# What is recursion?
##
## One of the coolest thing about functions are they can call another
## functions. Now in recursion, we create such a function which calls
## itself.
##
## Let us write some basic recursion function:
##
# ``` python

# def myfunc(name):
#     print("Hello, ", name, "!!");
#     myfunc(name)
#
# myfunc("Test")
#
# ```
## The code above will give an error after executing as this recursively
## call the function name till infinity and can cause damage to any
## system so they have handle raised an error for us and stopped the
## program to quit.
##
## So What are we missing here?
## You need three things to make recursion work properly as intended and
## they are as follows:
##
## 1. Base Case (i.e., when to stop)
## 1. Work toward Base Case
## 1. Call the function recursively.
##
## Now let us acutally see the example of the same:
##

def factorial(n):
    if n == 0:
        return 1;
    else:
        return (n) * factorial(n-1)

n = int(input("Enter a number: "));
print(factorial(n))


