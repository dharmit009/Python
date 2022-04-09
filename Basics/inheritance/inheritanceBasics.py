class A:
    def displayA(self):
        print("Display A!!!");

class B(A):
    def displayB(self):
        print("Display B!!!");


def main():
    testObjOfB = B();

    # calling displayA from test object of B ...
    testObjOfB.displayA();

    # calling displayB from test object of B ...
    testObjOfB.displayB();


if __name__ == '__main__':
    main();
