a = [ 5, 6, 7, 8, 9, 10, 11, 12,]
b = [ 1, 2, 3, 4, 5, 6, 7, 8,]
common=[]

print("A: ", a);
print("B: ", b);

for x in a:
    for y in b:
        if x==y:
            common.append(x);
print("Common Elements: ", common)
