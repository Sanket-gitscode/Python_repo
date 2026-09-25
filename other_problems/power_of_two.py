def power_of_two(number : int):
    
    current = 1
    
    while current <= number:
        
        if current == number:
            return True
        
        current = current * 2 
        
    return False
    
def isPowerOfTwo( n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0
        
    
#tets case 01 
x = 8

print(power_of_two(x))
print(isPowerOfTwo(16))