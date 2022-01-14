import sys
import menu
import player

def main():
    if "-h" in sys.argv or "--help" in sys.argv:
        menu.help_menu()
    else:
        choice = menu.menu()
        menu.setChoice(choice)


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

if __name__ == "__main__":
    main()
