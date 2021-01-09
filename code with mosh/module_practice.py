
def find_max(numeber):
    maximum = 0
    for i in number:
        if i > maximum:
            maximum = i
    return maximum

number = [10,9,11,8,2,4,0,-5]

print(f"maximum value is:{find_max(number)}")
