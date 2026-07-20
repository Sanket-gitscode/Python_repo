def longest_common_prefix(strings: list[str]) -> str:

    if not strings:
        return ""

    check_word = min(strings, key=len)

    for i in range(len(check_word)):

        for word in strings:

            if check_word[i] != word[i]:
                return check_word[:i]

    return check_word
        
#Test case 01 
strs = ["flower","flow","flight"]
print(longest_common_prefix(strs))

#Test case 02 

str2 =['dog','dog','dog']
print(longest_common_prefix(str2))