#python program to find sequence of lowercase letters joined with a underscore

import re

def text_match(text):
    pattern = '^[a-z]+_[a-z]+$' #no space

    if re.search(pattern, text):
        return "Text matched"
    else:
        return "Text does not matched"
if __name__ == "__main__":

    print(text_match("aab_cbbbc"))
    print(text_match("aab_ABBBC"))
    print(text_match("Aaab_cbbbc"))
    