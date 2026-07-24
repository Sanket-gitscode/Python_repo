def length_of_last_word(string : str):
    
    length = 0 
    idx = len(string) - 1
    
    
    while idx >= 0 and string[idx] == ' ':
            idx -= 1
    
    while idx >= 0 and string[idx] != ' ' :
        length += 1 
        idx -= 1 
    
    return length




#Test case 01 
text = "Hello world"
print(length_of_last_word(text))