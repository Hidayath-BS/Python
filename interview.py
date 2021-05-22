def adding(a, b):
    while b != 0:
        d = a & b
        a= a^b
        b = d << 1
    return a

print(adding(111,119))


# def max(numbers):
#     l=len(numbers)
#     count=0
#     res=numbers[0]
#     for i in range(l):
#         curcount=1
#         for j in range(i+1,l):
#             if numbers[i] != numbers[j]:
#                 break
#             curcount +=1
#         if curcount > count:
#             count=curcount
#             res=numbers[i]
#
#     return res
#
#
# x=[11,1,1,1,1,2,3,3,3,3,3,2,2,2]
# print(max(x))