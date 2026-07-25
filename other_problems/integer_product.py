n = 32 

def maxProduct1( n: int) -> int: 
    
    listn = list(map(int,str(n))) 
    total = 1 
    for nums in listn: 
        total *= nums 
    
    return total

def maxProduct2(n: int) -> int:
    product = 1
    for digit in str(n):
        product *= int(digit)
    return product

def maxProduct3(n: int):
    total = 1
    while n > 0 :
        last_digit = n % 10 
        total = total * last_digit 
        n = n // 10 
    return total        

def maxProduct4(n: int) -> int:
    
    first = 0
    second = 0

    while n > 0:
        digit = n % 10
        n //= 10

        if digit >= first:
            second = first
            first = digit
        elif digit > second:
            second = digit

    return first * second