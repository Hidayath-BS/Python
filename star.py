n = 5
for i in range(n+1):
    print(" "*(n-i), "*"*i)


for i in range(n+1):
    print("*"*i)


k=n
for i in range(n+1):
    for j in range(k):
        print(end=' ')
    k-=1
    for j in range(i+1):
        print("* ", end='')
    print()