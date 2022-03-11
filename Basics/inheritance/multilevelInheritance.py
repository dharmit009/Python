class A:
    def displayA(self):
        print("Hello From A");


class B(A):
    def displayB(self):
        print("Hello From B");


class C(B):
    def displayC(self):
        print("Hello From C");


def main():
    # creating a obj from class C  ...
    myMultilevelObjC = C(); 

    # Using `obj C` to call all the inherited methods ...
    myMultilevelObjC.displayA(); 
    myMultilevelObjC.displayB(); 
    myMultilevelObjC.displayC(); 


if __name__ == '__main__':
    main();
