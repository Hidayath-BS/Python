# FUnction argument
def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("average is: ", sum / len(numbers))

average(3,6,12,11,1)