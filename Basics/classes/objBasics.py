## class starts here ...
class Sq:

    def __init__(self):
        side = int(input("Enter the length of the side: "));

    ## functions aka methods ...
    def length(self):
        print("Side of a Square: ", self.side);


    def area(self):
        print("Area of Square: ", self.side**2);


    ## class ends here ...

## main program ...
square1 = Sq();

square1.length();
square1.area();

square2 = Sq();
square2.area();
