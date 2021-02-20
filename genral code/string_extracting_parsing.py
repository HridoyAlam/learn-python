'''
text = 'from maritin.lutherar@us.ac.bs Sat 06 02 2012'

atpos = text.find('@')
print(atpos)

next_space = text.find(" ", atpos)
print(next_space)

domain = text[atpos+1:next_space]
print(domain)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])
'''
text = "X-DSPAM-Confidence:    0.8475"
valu = text.find(".")

space = text[valu-1:valu+5]
print(float(space))