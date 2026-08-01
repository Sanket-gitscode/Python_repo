def next_permutation(array : list[int]) -> list[int]:
    
    n = len(array)
    
    i = n - 2 
    while i >=  0 and array[i] >= array[i+1]:
        i = -1
    
    if i >= 0 :
        j = n-1 
        while array[j] <= array[i]:
            j -= 1 
        
        array[j],array[i] = array[i],array[j]
    
    left = i + 1 
    right = n -1 
    
    while left < right :
        
        array[left],array[right] = array[left],array[right]
        left +=  1 
        right -= 1
    
    return array
        
arr = [1,2,3]
print(next_permutation(arr))