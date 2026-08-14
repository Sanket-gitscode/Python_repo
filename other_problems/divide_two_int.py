def divide(dividend,divisor):
    
    if dividend == -(2**31)  and dividend == -1 :
        return 2**31 -1 
    
    #we check if negative using XOR see xor give TRUE or 1  only when one of  is true
    
    negative = (dividend < 0 ) ^ (divisor < 0) 
    
    a = dividend
    b = divisor
    
    result = 0 
    
    while a >= b:
        
        temp = b 
        multiple = 1 
        
        while a >= (temp << 1):
            temp <<= 1 
            multiple <<= 1 
            
        a -= temp
        result += multiple
    
    return -(result) if negative else result
    

print(divide(43,3))