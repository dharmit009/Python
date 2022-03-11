
class Number:

    def getData(self):
        self.n1=int(input("Enter number 1: "))
        self.n2=int(input("Enter number 2: "))


class Multiplication(Number):

    def display(self):
        return self.n1 * self.n2;

mul1 = Multiplication();
mul1.getData();
out = mul1.display();
print(out)
