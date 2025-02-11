def div(a, b):
    x = a//b
    print(x)


a = int(input("Enter a value from 0-100"))
b = int(input("Enter b value from 0-100"))

try:
    div(a, b)

except ZeroDivisionError:
    print("can not divide by zero")
