def longest_substring(string):
    
    left = 0 
    max_len = 0 
    seen = set()
    
    for right in range(len(string)):
        
        while string[right] in seen:
            seen.remove(string[left])
            left += 1
            
        seen.add(string[right])
        
        if right - left + 1 > max_len:
            max_len = right - left + 1 
            
    
    return max_len
    

Input = "abcabcbb"
print(longest_substring(Input))