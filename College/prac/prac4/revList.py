# Q4.2: Accept 5 integer inputs from the user and store them in a list. Now, copy all the elements in another list but in reverse order.

a = [];
b = [];
for x in range(5):
    userin = int(input("Enter number: "));
    a.append(userin);

print("A: ", a);

for x in reversed(a):
    b.append(x);


print("B: ", b);
