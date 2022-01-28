""" write a program to create user defined function with *args that allows
user to pass integer numbers and perform addition. 
"""

def additioner(*args): 
	out = 0; 
	for x in range(len(args)): 
		out += args[x];

	print("Sum of numbers = ", out);

additioner(1, 5, 3, 1);

	
