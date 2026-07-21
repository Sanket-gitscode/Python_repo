def remove_element(array: list[int], val: int) -> int:
    write = 0

    for read in range(len(array)):
        if array[read] != val:
            array[write] = array[read]
            write += 1

    return write


# Test
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

k = remove_element(nums, val)

print(k)          # 5
print(nums[:k])   # [0, 1, 3, 0, 4]