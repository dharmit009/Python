import random
from colorama import Fore


def chooseState(A, B):
    A.winning_state = str(input("Choose Odd or Even [o/e]: ").lower())
    if A.winning_state != "o" and A.winning_state != "e":
        print("Error [E]: Invalid Option !!")
    else:
        A.displayNumber()
        B.displayNumber()
        resulter(A, B)


class Player:
    def __init__(self, name="CPU", number=None, winning_state=None):
        self.name = name
        self.number = number
        self.winning_state = winning_state

    def displayName(self):
        print(self.name.capitalize(), "\t:", self.number)

    def displayNumber(self):
        if self.name != "CPU":
            self.number = int(input("Enter A Number : "))
        else:
            self.number = random.randint(0, 100)

        displayName()


def resulter(A, B):
    additioner = int(A.number + B.number)

    print(Fore.RED, "\nAddition: ", additioner)
    if additioner % 2 != 0 and A.winning_state == "o" or A.winning_state == "odd":
        print(Fore.YELLOW, A.name, " Wins !!", sep="")
    elif additioner % 2 == 0 and A.winning_state == "e" or A.winning_state == "even":
        print(Fore.YELLOW, A.name, " Wins !!", sep="")
    else:
        print(Fore.GREEN, "CPU Wins !!", sep="")


name_of_player = input("Enter Your Name: ")
p1 = Player(name_of_player)
p2 = Player()

chooseState(p1, p2)
