#fibonnacci series till given digit

def fib(n):
    a=0
    b=1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range (1, n+1):
            print(a)
            c=a+b
            a=b
            b=c

fib(9)


