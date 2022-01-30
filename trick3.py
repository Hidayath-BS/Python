# find the most frequent value in the list
a = [1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1]
print(max(set(a), key=a.count))




# from collections import Counter
# cnt = Counter(a)
# print(cnt.most_common())
