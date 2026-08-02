def power(a,b):
    
    if b == 0 :
        return 1
    return a * power(a,b-1)

print(power(2,3))



def power2(base, exp):
    # Base case: anything to the power of 0 is 1
    if exp == 0:
        return 1
    
    # Handle negative exponents
    if exp < 0:
        return 1 / power2(base, -exp)
    
    # Recursive step: divide the exponent by 2
    half = power2(base, exp // 2)
    
    # If the exponent is even
    if exp % 2 == 0:
        return half * half
    # If the exponent is odd
    else:
        return base * half * half


# Example usage:
result = power2(2, 3)
print(result)  # Output: 8



def power_fast(a, b):
    # 1. Base case
    if b == 0:
        return 1
    
    # 2. Calculate the half-way point ONCE and save it
    half = power_fast(a, b // 2)
    
    # 3. If b is even (like 4), just return half * half (e.g., 2^2 * 2^2 = 2^4)
    if b % 2 == 0:
        return half * half
    
    # 4. If b is odd (like 3), we have an extra 'a' left over, so multiply by 'a'
    else:
        return a * half * half

print(power_fast(2, 3)) # Output: 8
print(power_fast(2, 4)) # Output: 16