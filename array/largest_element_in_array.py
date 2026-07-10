#finding largest element in array:


def largest_element_in_array(array : list[int]):
    
    #edge case:
    if not array:
        return None
    
    largest_number = array[0]
    
    for number in array[1:]:
        if number > largest_number:
            largest_number = number
            
    return largest_number
    
    
#test case 01 
nums1 = [3, 7, 2, 9, 1]
print(largest_element_in_array(nums1))

#test case 02 : negative elements 
nums2 = [-10, -5, -20, -1]
print(largest_element_in_array(nums2))