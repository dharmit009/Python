class UserOfWebsite:

    def __init__(self):
        self.x = input("Enter Your Name: "); 
        self.y = input("Enter Your Username: ");

    def display(self):
        print("Name: ", self.x); 
        print("Username: ", self.y); 


user1 = UserOfWebsite();
user1.display();
