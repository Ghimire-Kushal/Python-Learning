import os
# this is used to declare the path
# specify directory (current folder)
path = "../Python"

files = os.listdir(path)

for file in files:
    print(file)