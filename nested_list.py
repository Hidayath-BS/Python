#square of list of even number withi 10
square = [x**2 for x in range(1, 10) if x%2 == 0]
print(square)

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in mat:
    for c in i:
        print(c,end=' ')
    print()
