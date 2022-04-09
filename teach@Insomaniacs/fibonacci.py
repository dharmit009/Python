"""

Fibonacci Series: 

    0 1
    1
1       1
1   2   1
1 3 2 3 1
1 4 6 6 4 1


"""

n = 0
n1 = 0
n2 = 1

rows=int(input("Enter number of rows: "));

while n < rows:
    out=n1+n2
    print(out, end=', ')
    n1 = n2
    n2 = out
    n+=1
print();



