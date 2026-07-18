def lumotop(array):
    
    pivot = array[-1]
    index = -1 
    
    for i in range(len(array)-1):
        if array[i] < pivot:
            index += 1 
            array[i],array[index]  = array[index],array[i]
            
    array[index+1],array[-1] = array[-1],array[index+1]
    
    return array
    
    
arr = [5, 13, 6, 9, 12, 11, 8]    
print(lumotop(arr))