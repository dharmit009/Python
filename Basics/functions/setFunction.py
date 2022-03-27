def display(my_data):
    # the display functions will print all the uniq values ... of a
    # given data.
    uniq = set(sorted(my_data));
    print(uniq);


a = [1,0,2,3,8,9,4,7,9,0,4,8,5,2,9,0,3,8,4,7,5,9,0,8,3,7,4,0,8,9,1,2,3,4,0,9,8,7,5,0,8,2,7,3,4,5,0,8]
display(a);

a = "Hello, World!"
display(a);
