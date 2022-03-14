
def fact(n):
    if not isinstance(n, int):
        return None
    if n<0:
        return None;
    elif n==0:
        return 1;
    else:
        return n * fact(n-1)

n = eval(input("Enter a number to find factorial: "));
print(fact(n))
