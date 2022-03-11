class apple:
    def disA(self, numOfApple):
        self.numOfApple = numOfApple; 

class banana:
    def disB(self, numOfBanana):
        self.numOfBanana = numOfBanana; 

# Inherting apple and banana within class fruits at once... 
class fruits(apple, banana):
    def total(self):
        print("Total number of fruits: ", self.numOfApple +
                self.numOfBanana); 


# Declaring main function ...
def main(): 

    # Creating obj `myFruits` from class fruit ...
    myFruits = fruits();
    # Setting num of fruits for each fruit ... 
    myFruits.disA(5); 
    myFruits.disB(3); 
    # Calling function `total()` ...
    myFruits.total();

if __name__ == '__main__':
    main();
