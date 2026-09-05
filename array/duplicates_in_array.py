def containsDuplicate(nums: list[int]) -> bool:
    
    seen = {}
    for num in nums:
        seen[num] = seen.get(num, 0) + 1

    for key, value in seen.items():
        if value > 1:
            return True
            
    return False


arr = [1, 2, 3, 4,1]

print(containsDuplicate(arr))
