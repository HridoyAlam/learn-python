# tp = ('green', 'red', 'blue')
# print(tp[2])
# print(tp)

# l = list()
# t = tuple()
# print(dir(l))
# print(dir(t))
# (x,y) = (4, 'fred')
# print(x)

# d = dict()
# d['csev'] = 2
# d['cwen'] = 4

# for (k,v) in d.items():
#     print(k,v)

# tups = d.items()
# print(tups)

#tuples are compareable

#print((0,1,2) <(5,1,2))

d = {'a':10, 'b':1, 'c':22}
# d.items()
# print(sorted(d.items()))

# t = sorted(d.items())
# print(t)

# for (k,v) in sorted(d.items()):
#     print(k,v)

#sorting using values instead of key
tmp = list()
for k,v in d.items():
    tmp.append((v,k))

print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)


x = (5, 1, 3)
y = (6, 0, 0) 

print(y>x)