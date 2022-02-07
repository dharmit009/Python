
userin = str(input("Enter a character odd or eve [o/e]: ").lower());
userin = userin[0];

print("Character which you entered: ", userin, "\n");

if userin != "o" and userin != "e":
    print(userin, '!= o or ', end="");
    print(userin, '!= e');
    print("Therefore, Error: Invalid Option !!");
else: 
    print(userin);


# Debugging block 
# print("DataType of userin: \t", type(userin));
# print("DataType of 'o': \t", type('o'));
# print('DataType of "o": \t', type("o"), "\n");

