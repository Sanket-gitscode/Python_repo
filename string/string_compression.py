def compress_string(string : str):
    
    result = []
    
    i = 0 
    
    while i < len(string):
        
        current_char = string[i]
        count = 1 
        
        while i+1 < len(string) and string[i+1] == current_char:
            count += 1 
            i +=  1
            
        result.append(current_char + str(count))   
        i+= 1 
        
    return ''.join(result)
    



s1 = "aabcccccaaa"
print(compress_string(s1))