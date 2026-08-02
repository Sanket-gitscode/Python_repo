def recursive_sum(number : int) -> int :
    
    #Base case validation
    if number == 0 : 
        return number   #returning a number a variable rather than just RETURN which would give NONE as 
    
    return number + recursive_sum(number - 1)  
    # for each call stack it goes like 4 + func(n-1) ie 3
    # for each call stack it goes like 3 + func(n-1) ie 2
    # for each call stack it goes like 2 + func(n-1) ie 2
    # for each call stack it goes like 1 + func(n-1) ie 0
    # at zero it should return the number itself rahter than just 'return' which would give NONE and give an error

print(recursive_sum(4))