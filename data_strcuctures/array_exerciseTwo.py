heros=['spider man','thor','hulk','iron man','captain america']

print(f'length of the array is: {len(heros)}')

heros.append("black panther")
print(heros)

heros.remove('black panther')
print(heros)


heros.insert(3,'black panther')
print(heros)

heros[1:3] = ['doctor strange']
print(heros)

heros.sort()
print(heros)