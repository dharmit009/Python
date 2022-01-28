"""
Write a program to input your friend’s names and their
phone numbers and store them in the dictionary as the
key-value pair. Perform the following operations on the
dictionary:

	a) Display the Name and Phone number for all your friends.
	b) Add a new key-value pair in this dictionary and
	display the modified dictionary
	c) Delete a particular friend from the dictionary
	d) Modify the phone number of an existing friend
	e) Check if a friend is present in the dictionary or not
	f) Display the dictionary

"""

friend_dict = dict(); 

numOfFriends = int(input("Enter number of records you want to enter: ")); 


for x in range(numOfFriends): 
	friend_name = input("Enter Friends name: "); 
	friend_no = int(input("Enter Friends number: "));
	friend_dict[friend_name] = friend_no;
print(friend_dict);

delete = input("Enter Friend name which you want to delete: "); 
friend_dict.pop(delete); 
print(friend_dict);

friend_dict.update(test3="384738");
print(friend_dict);

if "test1" in friend_dict:
	print("Friend present in the dictionary"); 
else: 
	print("Friend not in dictionary"); 


