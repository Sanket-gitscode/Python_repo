def binary_search(array : list[int], target : int ):
    
    left = 0 
    right = len(array) - 1 
    
    while left <= right :
        
        mid = left + (right - left) // 2
        
        if array[mid] == target :
            return mid 
        
        elif array[mid] < target :
            left = mid + 1 
        
        else: 
            right = mid - 1
            
#test case 01 
arr = [4, 9, 15, 21, 28, 35, 42, 57, 63, 78, 91]
tg = 57

print(binary_search(arr,tg))