for i in [5,4,2,3,2]:
    print(i)
print("Blastoff!")

#list and difinite loop
frinds = ['jospes', 'green', 'sally']
for frnd in frinds:
    print(f"Happy new : {frnd}")
print("done")

#using the Range Function

print(range(4))
print(range(len(frinds)))

# A tale of two loops
for frined in frinds:
    print(f"Happy new year: {frined}")

for i in range(len(frinds)):
    fr = frinds[i]
    print(f"Happy birthday halaput:{fr}")
print("done")

stuff = list()
print(stuff)
stuff.append('Book')
stuff.append(69)
print(stuff,"\n")
print(9 in stuff)
print(stuff.sort())