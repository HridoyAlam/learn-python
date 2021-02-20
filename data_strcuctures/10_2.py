name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
tp = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    line = line.split()
    line = line[5]
    line = line[0:2]
    tp[line] = tp.get(line,0) + 1
        
ls = list()
for k,v in tp.items():
    ls.append((k,v))

ls.sort()

for v, k in ls:
    print(v,k)

