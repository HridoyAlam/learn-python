counts =  dict()
line = input("Enter a line of text:")
words = line.split()
print(f"words: {words}")
print("counting")

for i in words:
    counts[i] = counts.get(i,0) + 1
print(f"Counts: {counts}")

for key in counts:
    print(key, counts[key])