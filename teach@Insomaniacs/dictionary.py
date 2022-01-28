
a = {
        "1" : "Start the game", 
        "2" : "Settings", 
        "3" : "Exit", 
}

print("Menu");
for x, y in a.items():
    print(x, y);

choice = input("Choose an option: ");
print("You choose: ", a[choice])

