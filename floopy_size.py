#floopy size program.
f = int(input("Enter the free floopy size\n"))
u = int(input("Enter the used floopy size\n"))
tot = f+u
print("The total size is", tot)
o = int(input("Enter the size of file to delete\n"))
if tot >= o:
    u = u - o
    f = tot - u
    print(f)
    n = int(input("Emter new file size"))
    f = f - n
    if f < n:
        print("out of memory")
    else:
        print("The available size is", f)
else:
    print("File size is out of range")
