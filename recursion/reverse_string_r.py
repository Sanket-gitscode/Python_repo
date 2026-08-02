def reverse_string(string : str) -> str:
    
    if string == '':
        return string
    
    return reverse_string(string[1:]) + string[0]

s = 'hello'
print(reverse_string(s))