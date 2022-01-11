import player
from rich.console import Console

global c
global choice
c = Console()
plus_line = "+---------------------------------------------------------------+"

banner = """{}
   ___      _     _    ___         _____                       
  / _ \  __| | __| |  / _ \ _ __  | ____| _   __ ___             
 | | | |/ _` |/ _` | | | | | '__| |  _|  \ \ / //  _\            
 | |_| | (_| | (_| | | |_| | |    | |___  \ V //  __/            
  \___/ \__,_|\__,_|  \___/|_|    |_____|  \_/ \____|            
                                                               
{}""".format(plus_line, plus_line)

def menu():
    message = """{}
1. Play Against Human.                                         
2. Play Against CPU.                                           
3. Exit
{}
""".format(banner, plus_line)
    c.print(message, end="", style="italic blue")
    choice = int(input("Choose option [1-3]: "))
    c.print(plus_line)
    return choice


def setChoice(choice):
    if choice > 0 and choice < 5:
        if choice == 1:
            c.print("1. HUMAN VS HUMAN")
            player.human()
        elif choice == 2:
            c.print("2. HUMAN VS CPU")
            player.cpu()
        else:
            c.print("3. EXIT")
            c.print(plus_line)
    else:
        c.print("Invalid Option!")


def help_menu():

    message="""
{}
Usage: python oddOrEve.py [OPTION]... 

To simply play the game do not provide any options. 

Options:
        -h -> To display this message. 

{}
    """.format(banner, plus_line)
    print(message)


