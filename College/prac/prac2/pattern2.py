n = int(input("Enter number of rows: "));

i = 1;
k = 1;

while i <= n:
    j = 1
    while j <= i:
        print(k, end=" ");
        j+=1;
        k+=1;
    print();
    i+=1;


