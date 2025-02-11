# s = "daslakndlaaaaajnjndibniaaafijdnfijdnsijfnsdinifaaaaaaaaaaafnnasm"
# print(s)
# a_len = len(s)
# found_a_len = 0
# keep_going = True
# while a_len>0 and keep_going:
#     aas = "a" * a_len
#     if aas in s:
#         found_a_len = a_len
#         keep_going = False
#     a_len=a_len -1
# print ("max length of a:" , found_a_len)
# keep_going = True
# while keep_going:
#     s=s.replace("aaa","aa")
#     if "aaa" not in s:
#         keep_going = False
# print(s)





# function to find out the maximum
# repeating character in given string
def maxRepeating(str):
    l = len(str)
    count = 0
    # Find the maximum repeating
    # character starting from str[i]
    res = str[0]
    for i in range(l):

        cur_count = 1
        for j in range(i + 1, l):

            if (str[i] != str[j]):
                break
            cur_count += 1

        # Update result if required
        if cur_count > count:
            count = cur_count
            res = str[i]
    return res


str = "aabbbbbssshhrrbba"
print(maxRepeating(str))
small=1000
big=1
e=str.split('1')
while "" in e:
    e.remove("")
for i in e:
    # print(len(i))
    if len(i) < small:
        small = len(i)
    if len(i) > big:
        big = len(i)
print("small is ",small)
print("big is ", big)


