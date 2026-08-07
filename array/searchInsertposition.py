def searchinsert(array : list[int], target : int) -> int:
    
    n = len(array)
    
    #single loop solution:
    for i in range(n):
        if array[i] > target:
            return i 
        
        elif array[i] == target:
            return i                    # whole line could be worte in one if we do just array[i] >= target
        
    return len(array)
    
    
nums = [1,3,5,6]
target = 4
print(searchinsert(nums,target))


################################################################

def searchinsert_binary(array,target):
   
    n = len(array)
    left = 0
    right = n 

    while left < right:

        mid = left + (right - left) // 2

        if array[mid] < target:
            left = mid + 1

        elif array[mid] >= target:
            right = mid
            
    return left
   
    
    
nums = [1,3,5,6]
target = 7
print(searchinsert_binary(nums,target))