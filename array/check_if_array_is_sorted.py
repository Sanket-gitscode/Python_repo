def is_sorted(array : list[int]):
    
    for i in range(1,len(array)):
        if array[i] < array[i-1]:
            return False
        
    return True
        
        
#Test case 01 
arr1 = [1, 2, 3, 4,6,5]
print(is_sorted(arr1))
    
