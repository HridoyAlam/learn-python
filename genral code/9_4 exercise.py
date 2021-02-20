name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)


li = list()

for line in handle:
    if not line.startswith("From:"):
        continue
    line = line.split()
    li.append(line[1])
counts = dict()
for i in li:
    counts[i] = counts.get(i,0) + 1
#print(counts)

bigcount = None
bigword = None
for word,count in counts.items(): 
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print (bigword,bigcount)