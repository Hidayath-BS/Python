#packing 8 hotdogs in single pack, how may package can be done for 400 hot dog.
print("Packing 8 hotdog ")
total = 0
final = 400
for i in range(1, 70):
    now = 8 * i
    if now <= 400:
        total = i


print("The total package is ", total)
