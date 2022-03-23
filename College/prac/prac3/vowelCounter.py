count=0;
vowels = ['a', 'e', 'i', 'o', 'u']

a = input("Enter a String: ")

for x in a:
    if x in vowels:
        count+=1;

print("Number of Vowels in String: ", count);

