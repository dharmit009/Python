startrange=eval(input("Enter Starting Range: "));
endrange=eval(input("Enter end Range: "));

for i in range (startrange, endrange):
    if i % 2 == 0:
        print(i,", ", end="");
print("");
