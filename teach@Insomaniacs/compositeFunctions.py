# What are composite functions?
##
## Composite functions are combination of more than one function i.e the
## function takes another function as an argument.
## Pre-requistes: lambda functions.
##
## In mathematical terms it could be denoted as: f(x) = f(g(x))
## Let us see how we can redefine the same in python syntax:
##

n = int(input("Enter a number: "));

def compose(f,g):
    return lambda x: f(g(x))

def double(x):
    return x*2;

def inc(x):
    return x+1;

compositor = compose(double, inc)
print(compositor(n))



