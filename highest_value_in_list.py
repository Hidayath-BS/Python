#taking highest value in list to last and print it.
lst = [66,57,54,53,64,52,59]
print(lst)
for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
        lst[i], lst[i+1] = lst[i+1],lst[i]
print(lst[len(lst)-1])
