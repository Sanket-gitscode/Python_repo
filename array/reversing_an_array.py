def reversing_array(array : list[int,str]):
    
    n = len(array)
    left_pointer = 0 
    right_pointer = n - 1 
    
    while left_pointer < right_pointer :
        array[left_pointer],array[right_pointer] = array[right_pointer],array[left_pointer]
        left_pointer  += 1
        right_pointer -= 1
        
    return array 
    
    
#Test case 01 
test_case_01 = [1,2,3]
print(reversing_array(test_case_01))