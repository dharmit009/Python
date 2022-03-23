n = eval(input("Enter a number: "));
divs = []

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            divs.append(i)

# print("Divs: ", divs)
# print("Length of Divs: ", len(divs))
if len(divs) > 0:
    print(n, " is not a prime number. ")
elif n <= 1:
    print(n, " is not a prime number. ")
else:
    print(n, " is a prime number. ")

