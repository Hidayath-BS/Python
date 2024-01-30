# finding common elements in 2 lists
# take 2 lists
scholar1=['Vinay', 'Krishna', 'Shah', 'Hidayath', 'Govind']
scholar2=['Rosy', 'Shah', 'Tanushri', 'Hidayath', 'Vishal']

# convert them into sets
s1=set(scholar1)
s2=set(scholar2)

# find intersection of the 2 sets
s3=s1.intersection(s2)

# convert the resultant set into a list
common=list(s3)

# dispaly the list
print(common)
