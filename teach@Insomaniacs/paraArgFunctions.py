# What are parameters and arguments in a function?
##
## This is one of the most outrageous things about which people often
## get wrong so I recommend you to pay attention.
##
## Let us start with defination of each of them:
##
## **Parameters:**
##
## Parameters are placeholders for variables or functions which may be
## passed while calling the function. (Note: Some paramters have default
## values so technically their values are not passed to the function).
##
## **Arguments:**
##
## **Arguments** are the actual values passed to the function.
##
## Let us see the difference:
##
## `name` stores the first value passed to the function
## Therefore `name` is a parameter.

def hello(name):
    print("Hello,", name);

hello("Sam") # The Word "Sam" is an argument.



