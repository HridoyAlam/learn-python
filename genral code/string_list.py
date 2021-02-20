abc = "with tree words"
stuff = abc.split()
print(stuff)
print(len(stuff), '\n')

line = "a lot           of spaces"
etc = line.split()
print(etc)

antoher_line = "first;second;third"
thing = antoher_line.split()
print(thing)
print(len(thing), '\n')

new_thing = antoher_line.split(';')
print(new_thing)
print(len(new_thing))

friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends)