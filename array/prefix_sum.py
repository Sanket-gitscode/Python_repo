def prefix_sum(array: list[int]):
    prefix = array.copy() #just in case to preserve the original array 

    for i in range(1, len(prefix)):
        prefix[i] += prefix[i - 1]

    return array, prefix


test01 = [2, 4, 1, 6, 3]

original, prefix = prefix_sum(test01)

print(original)  # [2, 4, 1, 6, 3]
print(prefix)    # [2, 6, 7, 13, 16]
print(test01)    # [2, 4, 1, 6, 3]