#list operation 
num = list(range(2, 10, 1))
for i in num:
    print(i)
num.append(450)
print(num)
num[1:4] = 320, 23, 21
print(num)
num.remove(320)
print(num[::-1])
print(num*2)
print(num.count(3))



numm = [2, 3, 5, 23, 54, 73]
s1 = set(num)
s2 = set(numm)
print(s1.intersection(s2))


