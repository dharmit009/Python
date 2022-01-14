import random
import main
from rich.console import Console

## GLOBALS
global choice
global c

# rich printer
c = Console()

# decoration for message
plus_line = "+---------------------------------------------------------------+"


class Player:

    def __init__(self, name="CPU", number=None, winning_state=None) -> None:
        self.name = name.upper()
        self.number = number
        self.winning_state = winning_state

    def set_number(self):
        if self.name != "CPU" and self.number == None:
            c.print("[{}]\t".format(self.name), end="", sep="")
            self.number = int(input("Enter a number: "))
        else:
            self.number = random.randint(0, 11)
        c.print(plus_line)
        c.print("Name:  \t", self.name)
        c.print("Number:\t", self.number)
        c.print(plus_line)


def set_winning_state(A, B):
    try: 
        c.print("[{}]\t".format(A.name), end="", sep="")
        A.winning_state = str(input("What do you choose odd or eve? [o/e]: ")).lower();
        if A.winning_state != 'o' and A.winning_state != 'e':
            raise;
        else: 
            if A.winning_state == 'o':
                B.winning_state = 'e'; 
            else:
                B.winning_state = 'o'; 
    except: 
        print("Error !! Invalid option selected ... Try Again ...");

def play(A, B):
    result = int(A.number + B.number)
    c.print("\nAddition: ", result, style="red")
    if result % 2 != 0 and A.winning_state == "o" or A.winning_state == "odd":
        c.print(A.name, " Wins !!", sep="", style="orange bold")
    elif result % 2 == 0 and A.winning_state == "e" or A.winning_state == "even":
        c.print(A.name, " Wins !!", sep="", style="orange bold")
    else:
        c.print(B.name, " Wins !!", sep="")


def human():
    p1_name = str(input("[P1] Enter Your Name: "))
    p2_name = str(input("[P2] Enter Your Name: "))

    p1 = Player(p1_name)
    p2 = Player(p2_name)

    set_winning_state(p1, p2)
    p1.set_number();
    p2.set_number();
    play(p1, p2);


def cpu():
    p1_name = str(input("[P1] Enter Your Name: "))

    p1 = Player(p1_name)
    p2 = Player()
    set_winning_state(p1, p2)
    p1.set_number();
    p2.set_number();
    play(p1, p2)




