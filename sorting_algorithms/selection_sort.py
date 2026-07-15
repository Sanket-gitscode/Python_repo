
def SelectionSort(array):
    
    for i in range(len(array)):
        
        min_index  = i 
        
        for j in range(i+1,len(array)):
            if array[j] < array[min_index]:
               min_index = j 
               
        array[min_index],array[i] = array[i],array[min_index]
        
    return array

arr = [29, 10, 14, 37, 13]
print(SelectionSort(arr))        
        