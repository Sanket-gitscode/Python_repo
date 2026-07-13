def rotate_arry_by_k(array : list[int], k : int):
    
    def array_reverse(array,left,right): # basic array reversal using two pointers technique 
        
        while left < right :
            array[left],array[right] = array[right],array[left]
            left  += 1
            right -= 1
            
    
    n = len(array) - 1
    
    k =  k %  n   # if k > n for wrapping around the array we use modulo 

    array_reverse(array,0,n)
    array_reverse(array,0,k)
    array_reverse(array,k,n)
    
    return array

# Test case
arr = [1,2,3,4,5]
k = 2
