dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}

print("Before Adding Dictionary !");
print("Dictionary 1: ", dic1);
print("Dictionary 2: ", dic2);
print("Dictionary 3: ", dic3);
print("Dictionary 4: ", dic4);
print("");

dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)

print("Dictionary 1: ", dic1);
print("Dictionary 2: ", dic2);
print("Dictionary 3: ", dic3);
print("Dictionary 4: ", dic4);
