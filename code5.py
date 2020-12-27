#remove lowercase substrirng froma given a string
import re

str1 = "AFNbsghgFJKHFNKHFLunffnskbgsk"
print("Orginal text")
print(str1)
remove_lower = lambda text:re.sub('[a-z]','',text)
result = remove_lower(str1)
print(result)