a = [ 5, 6, 7, 8, 109, 1, 12, 1, 314, 5, 116, 117, 120]

print("a =", a);

print("");
print("METHOD 1: ");
maxi = a[0]
mini = a[0]

for x in a:
    if x < mini:
        mini = x;

print("Minimum: ", mini);

for x in a:
    if x > maxi:
        maxi = x;

print("Maximum: ", maxi);

print("");
print("METHOD 2: ");
# alternative method.
maximum = max(a);
minimum = min(a);

print("Minimum: ", minimum);
print("Maximum: ", maximum);
