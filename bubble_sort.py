# sorting the list using bubble sort
# create an empty list to sort the elements
x=[]

#store the elements in the list x
print('how many elements?', end='')
n=int(input())   # accept the input into n

for i in range(n):
    print('the elemnts are:', end='')
    x.append(int(input()))   # add the elements into the list x

print('original list:', x)

#bubble sort

flag = False                            #when swapping is done flag becomes True
for i in range(n-1):                    # i is from 0 to n-1
    for j in range(n-1-i):              # j is from 0 to one element lesser than i
        if x[j]>x[j+1]:                 # if first element is bigger than 2nd one
            t=x[j]                      # swap j and j+1 elements
            x[j]=x[j+1]
            x[j+1]=t
            flag=True                   #swapping done, hence flag is True
    if flag==False:                     #no swapping means list is in sorted order
        break                           # come out of inner loop
    else:
        flag=False                      # assign initial value to flag
print('sorted list:', x)
