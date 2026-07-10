def find_max_consecutive_ones(array: list[int]):
    
    count = 0 
    max_count = 0 
    
    for num in array:
        if num == 1:
            count += 1 
            if count > max_count :
                max_count = count
            
        else:
            count = 0 
        
    return max_count


nums = [1, 1, 0, 1, 1, 1]
print(find_max_consecutive_ones(nums))

# new test case:
nums2 = [0,0,0]
print(find_max_consecutive_ones(nums2))