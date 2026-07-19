def longest_common_prefix(strings : list):
    
    check_word = strings[0]   #word use to check with other in strings

    for i in range(len(check_word)):
        for j in strings[1:]:
            if  i >= len(j) or check_word[i] != j[i]:
                return check_word[:i]
                      
        
        
#Test case 01 
strs = ["flower","flow","flight"]
print(longest_common_prefix(strs))