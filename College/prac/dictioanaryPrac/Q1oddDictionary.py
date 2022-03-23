"""
		Create a dictionary ‘ODD’ of odd numbers between 1 and 10, where the
		key is the decimal number and
		the value is the corresponding number in words.
		Display the keys in dictionary ‘ODD’.
		Display the values in dictionary ‘ODD’.
		Display the items from dictionary ‘ODD’
		Find the length of the dictionary ‘ODD’.
		Check if 7 is present or not in dictionary ‘ODD’
		Retrieve the value corresponding to the key 9

"""

odd={
	1:"One",
	3:"Three",
	5:"Five",
	7:"Seven",
	9:"Nine"
}

print("Keys: ");
for key in odd.keys():
	print(key, sep=", ", end=" ");
print("");

print("Values: ");
for values in odd.values():
	print(values, sep=",", end=" ");
print("");
print("");


print("Dictionary: ");
for x, y in odd.items():
	print(f"{x}: {y}");
print("");

if 7 in odd:
	print("Seven is present");

print(odd.get(9))


