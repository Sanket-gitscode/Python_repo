def is_anagaram(string1 : str , string2 : str):
    
    if len(string1) != len(string2):
        return False
    
    char_freq = {}
    
    for ch in string1:
        
        char_freq[ch] = char_freq.get(ch,0) + 1
    
    
    for ch in string2:
        if ch not in char_freq:
            return False
        
        char_freq[ch] -= 1
        
        if char_freq[ch] < 0 :
            return False
    
    return True 

#Test case 01 
s1 = "silent"
s2 = "listen"
     
print(is_anagaram(s1,s2))