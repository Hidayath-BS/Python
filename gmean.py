# using user defined functions to calculate gmean AND greater value
def gmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)

def isgreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("second number is greater")


isgreater(a=4,b=8)
gmean(a=4,b=8)

