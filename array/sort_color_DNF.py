def sortcolor(array : list[int]) -> list[int]:
    
    n = len(array)
    low = 0 
    mid = 0 
    high = n- 1 
    
    while mid <= high :  # Not binary search algo requires to compare MID with HIGH as MID is the explorer
        
        if array[mid] == 0: # 0 belongs to low (left side) and mid is 1 
            array[mid], array[low] = array[low],array[mid]
            low += 1 
            mid += 1 
        
        elif array[mid] == 1: # as we assumed mid is 1 its correct position so we just move th pointer 
            mid += 1 
            
        else: # mid = 2  meaning value belong to right that is high which is 2 soo we swap with high and move from right to left meaing high -1 
            array[mid],array[high] = array[high],array[mid]
            high -= 1
            
    return nums

nums = [2, 0, 2, 1, 1, 0]
print(sortcolor(nums))