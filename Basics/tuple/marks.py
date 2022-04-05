n=int(input("Enter the number of students: "))
for i in range(n):
    marks=()
    name=input("Enter your name: ")
    m1=int(input("Enter marks in first subject: "))
    m2=int(input("Enter marks in second subject: "))
    m3=int(input("Enter marks in third subject: "))
    marks+=(m1,m2,m3)
    print(name,", Your Total sum of all three subjects is:",sum(marks))
