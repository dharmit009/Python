a = [1,2,2]

print("Length of List: ",len(a));

print("Size of a: ", len(a))

for eachx in a:
    if eachx % 2 == 0: 
        print(eachx)

print("Range Function: ")
for x in range(0,10):
    print(x)

a.sort()
print(a)

friends = ["Kevin", "Jim", " Smith", "Oscar", "Toby", "Jim", "Harry"]
# friends.sort()
friends.pop()
print(friends)
friends.insert(3, "Meet")


