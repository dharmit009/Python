import math
# What are Functions?

## Functions: Function Calls, Type Conversion Functions, Math Functions, Composition, Adding
## New Functions, Definitions and Uses, Flow of Execution, Parameters and Arguments,
## Variables and Parameters Are Local, Stack Diagrams, Fruitful Functions and Void Functions,

## Why Functions?Importing with from, Return Values,
## More Recursion,

## NEED TO LEARN:
## Incremental Development, Composition, Boolean Functions, Leap of Faith, Checking Types

def helloWorld():
    print("Hello World!!")

n = int(input("Enter a number: ")); # Type conversion functions.
print("Power of 2: ", pow(n,2)) # Math functions.

# What are lambda functions?
##
## Lambda functions are anonymous functions which are generally
## expressions defined in a single line. A Lambda function consist of input
## and return value. That's all though they largely decrease the
## readability of the code. A lambda function can multiple inputs as
## well as multiple return values.

double = lambda x: x*2;
print("Doubler: ", double(n));



