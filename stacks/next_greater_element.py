def next_greater_element_forward(nums):
    
    n = len(nums)
    result = [-1] * n
    stack = []
    
    for i in range(n):
        
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
            
        stack.append(i)
        
    return result
            
    
# Example usage:
nums = [4, 5, 2, 25]
print(next_greater_element_forward(nums))  # Output: [5, 25, 25, -1]