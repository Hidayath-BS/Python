# printing patters ** in two times in row.

s = "**"
space = " "
k=6
for l in range(6):
    for i in range(2):
        print(space*(6-l), s * l)

