a = [ 23, 42, 'a', 'test', 3, 'b']
print("A: ", a);
for x in a:
    x = str(x)
    if x.isnumeric():
        print(x);
        print(x);
        print(x);
    else:
        print(x+' #');
