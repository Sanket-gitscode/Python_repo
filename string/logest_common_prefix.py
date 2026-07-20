def longest_common_prefix(strings : list):
    
    if len(strings) < 1 :
        return False
    
    check_word = strings[0]
    
    for i in range(len(check_word)):
        for j in strings[1:]:
            if i >= len(j) or check_word[i] != j[i]:
                return check_word[:i]
    
    return check_word
        
#Test case 01 
strs = ["flower","flow","flight"]
print(longest_common_prefix(strs))

#Test case 02 

str2 =['dog','dog','dog']
print(longest_common_prefix(str2))