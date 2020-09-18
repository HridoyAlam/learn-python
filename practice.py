'''
nums = [1,2,3]
print(nums + [4,5,6])
print(nums * 3)

words = ["spam", "egg", "chikem", "meat"]
print("spam" in words)
print("tea" in words)

nums = [10,9, 8, 7, 6, 5]
nums[0] = nums[1]-5

if 4 in nums:
    print(nums[3])
else:
    print(nums[4])
print(nums)


nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

#list functions
nums = [1, 1, 2, 3]
nums.append(4)
#print(nums)
#print(len(nums))
index = 1
nums.insert(index,9)
print(nums)
#print(nums. index(9))
print( max (nums))
print( min (nums))
print(nums.count(1)) #list.count(item)
nums.remove(9)
print(nums)
nums.reverse()
print(nums)


#while loops
i = 1
while i<= 5:
    print(i)
    i = i+1
print("finished")
'''
i = 3
j = 0
while i >= 0:
    print(i)
    i -=1
    j +=1
print(j)