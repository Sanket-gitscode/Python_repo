def is_array_palindrome(array : list[int]):
    
    left = 0 
    right = len(array) - 1
    
    while left < right:
        if array[left] != array[right]:
            return False
        left += 1
        right -= 1
        
    return True
        
    
    
#Test case 01 
test01 = [1,2,3,2,1]    
print(f'''the given array is a "{is_array_palindrome(test01)}" palindrome''')
#Test case 02 
test02 = [1,2,3]
print(f'''the given array is a "{is_array_palindrome(test02)}" palindrome''')