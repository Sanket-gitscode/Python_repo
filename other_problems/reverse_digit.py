def reverse_digit(number):
    
    sign = -1 if number < 0 else 1 
    
    reversed_number = 0 
    
    number = abs(number)
    
    while number > 0 :
        
        last_digit  = number % 10 
        number = number // 10 
        reversed_number = reversed_number * 10 + last_digit 
        
    
    return reversed_number * sign
    
    
    
#Test case 01 
digit = -123 
print(reverse_digit(digit))