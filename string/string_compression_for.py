#using for loop 

def compress_string(string : str):

    if not string:
        return ''
    
    result = []
    count  = 0 
    
    for i in range(len(string)):
        
        count += 1 
        
        if i+1 == len(string) or string[i] != string[i+1]:
            result.append(string[i]+ str(count))
            count = 0 
    
     
    result_string =  ''.join(result)

    return result_string if len(string) > len(result_string) else string


s1 = "aabcccccaaa"
print(compress_string(s1))