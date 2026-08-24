def string_to_int(string : str) -> int:
    
    result = 0 
    started = False
    sign = 1  
    
    for ch in string:
        
        if started is False and ch.isspace():
            continue
        
        if started == False:
            if ch == "-":
                sign = -1 
                continue
            
            if ch == "+":
                sign = 1 
                continue
        
        if not ch.isdigit():
            break
    
        started = True
        
        ch_in_int = int(ch)
        
        result = result * 10 + ch_in_int
        
    result = result * sign

    if result > 2147483647:
        return 2147483647

    if result < -2147483648:
        return -2147483648

    return result
        


s = '989887778787'

print(string_to_int(s))