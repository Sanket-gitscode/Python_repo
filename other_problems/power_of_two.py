def power_of_two(number : int):
    
    current = 1
    
    while current <= number:
        
        if current == number:
            return True
        
        current = current * 2 
        
    return False
    
    
#tets case 01 
x = 10

print(power_of_two(x))