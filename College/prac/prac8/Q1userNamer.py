"""
Q1. Write a program that uses a user defined function that accepts name and
gender(M or F)and prefix Mr/Mrs on the basis of the gender. 

"""

def user_name(name, gender): 
	if gender == 'm':
		base="Mr."
		print(base,name); 
	elif gender == 'f': 
		base="Mrs."
		print(base, name);
	else: 
		print("Error"); 


name = input("Enter your name: ").lower();
gender = input("Enter your gender [m/f]: ").lower(); 
user_name(name, gender);
