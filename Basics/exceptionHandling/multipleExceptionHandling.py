try:
    a = 5;
    b = 0;
    print(a/b);

except TypeError:
    print("Unsupported Operation ...");
except ZeroDivisionError:
    print("Division By Zero is Not Allowed ...");

