def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # value → index
    
    for i, num in enumerate(nums):
        needed = target - num  # What do I need?
        
        if needed in seen:
            return [seen[needed], i]
        
        seen[num] = i  # Store for future
    
    return []  # No solution found


nums = [3, 2, 4]
target = 6
print(two_sum(nums, target))

# New test case
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))