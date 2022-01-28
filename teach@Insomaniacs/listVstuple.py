mylist = [1,2,3,4,5]
mytuple = (1,2,3,4,5)

print("Before ... "); 
print(mylist[0])
print(mytuple[0])

try: 
    mylist[0] = 2
    mytuple[0] = 2

except: 
    print("After: ");
    print(mylist[0])
    print(mytuple[0])
