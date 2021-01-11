from pathlib import Path

#path = Path('ecomerce1')
#print(path.exists())

#create new dirctory

#path = Path('ecomerce1')
#print(path.mkdir())

# remove directory

#path = Path('ecomerce1')
#print(path.rmdir())

#find all files in giving directory

path = Path()
#for file in path.glob('*.py'):
for file in path.glob('*.*'):    
    print(file)