# insert into dict and search for key

x = {}
n = int(input("Enter the number of values"))

for i in range(n):
    k = input("Enter the key :")
    v = input("Enter the value :")
    x.update({k: v})

for name in x.keys():
    print(name)

search = input("Enter to search")

found = x.get(search, -1)
print(found)