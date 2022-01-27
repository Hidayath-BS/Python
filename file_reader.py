#read file from alice.txt and print linnes use with open.
filename = 'alice.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
