# Global and Local Variables:
##
## Global variables are accesible anywhere within the program. Whereas
## the local variables cannot be accessed once they are out of scope.
##
## Here is a small example:
##

x = 5

def foo():
    x = 10
    print("local x:", x)


foo()
print("global x:", x)
