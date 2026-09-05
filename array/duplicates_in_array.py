def containsDuplicate(nums: list[int]) -> bool:
    
    seen = {}
    for num in nums:
        seen[num] = seen.get(num, 0) + 1

    for key, value in seen.items():
        if value > 1:
            return True
            
    return False

def contains_duplicate(array : list[int]):
    
    seen = set()
    
    for num in array:
        if num in seen:
            return True
        seen.add(num)
        
    return False


arr1 = [1, 2, 3, 4, 1]
arr2 = [1,2,3,4]

#Testing both code 

#c1 
print(containsDuplicate(arr1))
print(containsDuplicate(arr2))

#c2
print(contains_duplicate(arr1))
print(contains_duplicate(arr2))