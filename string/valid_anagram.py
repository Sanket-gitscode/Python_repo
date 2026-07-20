def is_valid_anagram(string1,string2):

    #base case:
    if len(string1) != len(string2):
        return False
    
    
    char_map = {}
    
    for ch in string1:
        char_map[ch] = char_map.get(ch,0) + 1 
        
    for ch in string2:
        if ch not in char_map:
            return False
        
        char_map[ch] -= 1

    
    return len(char_map) == 0
    
s1 = 'silent'
s2 = 'listen'

print(is_valid_anagram(s1,s2))