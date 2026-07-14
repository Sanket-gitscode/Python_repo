def lumto_partition(array : list[int]):
    
    pivot = array[-1]
    i = - 1
    
    for j in range(len(array) - 1 ):
        if array[j] < pivot:
            i += 1 
            array[j],array[i] = array[i],array[j]
    

    array[i+1],array[-1] = array [-1],array[i+1]
    
    return array
    
#Test case 01 
arr = [9, 3, 7, 1, 8, 2, 5, 6, 4]
print(lumto_partition(arr))