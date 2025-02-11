# binary = "01001000111010000011"
# binary = "0100100011100000000000000010000011"
binary = "11111011101001000000000000000000010001"

data = binary.strip('1').split("1")
new = []
neww = []
for i in data:
	if i == '':
		continue
	else:
		new.append(i)
		neww.append(len(i))
# print(data)
# print(new)
# print(neww)
min = neww[0]
max = neww[0]
for x in neww:	
	if x < min:
		min = x
	if x > max:
		max = x
print(min)
print(max)



