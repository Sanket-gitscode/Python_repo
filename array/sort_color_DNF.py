def sortcolor(array : list[int]) -> list[int]:
    
    n = len(array)
    low = 0 
    mid = 0 
    high = n- 1 
    
    while mid <= high :
        
        if array[mid] == 0:
            array[mid], array[low] = array[low],array[mid]
            low += 1 
            mid += 1 
        
        elif array[mid] == 1: 
            mid += 1 
            
        else: # mid = 2 
            array[mid],array[high] = array[high],array[mid]
            high -= 1
        
    return nums


nums = [2, 0, 2, 1, 1, 0]
print(sortcolor(nums))