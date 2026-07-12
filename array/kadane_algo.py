def kadane_algorithm( array: list[int]):
    
    current_sum = array[0]
    max_sum = current_sum
    
    for number in array[1:]:
        if current_sum + number  > number:
            current_sum = current_sum + number
        else:
            current_sum = number 
        
        if current_sum > max_sum:
            max_sum = current_sum
        
    return max_sum
    

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(kadane_algorithm(nums))