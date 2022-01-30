# reverse a given string
a = 'abcdefghijklmnopqrstuvwxyz'
print(a[::-1])

# using for loop
for char in reversed(a):
    print(char, end='')

# for integer value
b = 1234567890
print(int(str(b)[::-1]))

