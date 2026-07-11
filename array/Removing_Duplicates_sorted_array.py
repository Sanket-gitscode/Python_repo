def remove_duplicates(nums: list[int]):
    slow = 0  # Points to last unique element

    for fast in range(1, len(nums)):
        # If we found a new unique element
        if nums[fast] != nums[slow]:
            slow += 1              # Move slow forward
            nums[slow] = nums[fast]  # Copy the new element here

    return slow + 1  # Count of unique elements


nums = [1,1,2,2,3]
print(f"Before duplicates remove : {nums}")

k = remove_duplicates(nums)
print(f"After duplicate removel {nums[:k]}")
print(f"Number of uniques element : {k}")
