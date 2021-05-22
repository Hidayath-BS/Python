# missing one number
def getMissingNo(A):
	n = len(A)
	total = (n + 1)*(n + 2)//2
	sum_of_A = sum(A)
	return total - sum_of_A


A = [1, 2, 4, 5, 6]
miss = getMissingNo(A)
print(miss)


# missing few numbers
def find_missing(lst):
	return [x for x in range(lst[0], lst[-1] + 1) if x not in lst]


lst = [1, 2, 4, 6, 7, 9, 10]
print(find_missing(lst))
