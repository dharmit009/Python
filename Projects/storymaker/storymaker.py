
base_line = "Once upon a time, There lived a "

ad = list();
for i in range(0,3):
    print("Adjective[{}] ".format(i), end="", sep="");
    userin=str(input("Enter a adjective: "))
    ad.append(userin)

location = input("Enter a place name: ")
something = input("Enter something you like to do: ")

print("")
out = base_line + ad[0] + f"in the mountains of {location},\nHe used to like {something} everyday.\nBut once day someone kicked him out.\nSo he started {ad[1]} {ad[2]}"
print(out)
