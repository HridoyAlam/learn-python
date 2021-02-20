ddd = dict()
ddd['a'] = 1
ddd['b'] = 2
ddd['c'] = 3
print(ddd)
ddd['c'] = -3
print(ddd)
print(ddd['a'])


counts = dict()
names = ['csev', 'cwen', 'csev', 'rewn', 'cwen']
for i in names:
    if i not in counts:
        counts[i] = 1
    counts[i] = counts[i]+1
print(counts)
'''
#the get method for dictionaries 
if name in counts:
    x = counts[name]
else:
    x = 0

#is equvalent to
x = counts.get(name, 0)

'''

counts = dict()
names = ['csev', 'cwen', 'csev', 'rewn', 'cwen']
for name in counts:
    counts[name] = counts.get(name, 0) + 1
print(counts)

stuff = dict()
print(stuff.get('candy',-1))