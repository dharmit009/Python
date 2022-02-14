import os 

loc = "/home/hmm/repos/python/Basics/functions"
filename = "test.md"

# automatically adds / to the path file name
with open(os.path.join(loc, filename)) as f:
    print(f.read())
