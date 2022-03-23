# Q2.6: WAP in python to count occurence of even number and odd number between the range(accept range start
# and end value from user)

start = int(input("Enter a start of the range: "));
end = int(input("Enter a end of the range: "));

odd, eve = 0, 0;

for x in range(start, end+1):
    if x % 2 == 0:
        eve += 1;
    else:
        odd += 1;

print("Number of odds: ", odd);
print("Number of even: ", eve);


