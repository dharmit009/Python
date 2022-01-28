""" Write a recursive function to calculate 
factorial of a number """

"""
LOGIC BUILDING: 

fact(3) = 3 * 2 * 1 = 6; 

""" 
def fact(n: int) -> int:
	if n == 0 or n == 1: 
		return 1; 
	elif n < 0: 
		print("Error [E]: Negative numbers don't have factorial"); 
		return 0;
	else: 
		return n * fact(n-1);


num = int(input("Enter a number: "));
fact = fact(num);
print(f"Factorial [{num}]: ", fact);





