def majority_element(array: list[int]):
    vote_count = 0
    candidate = None

    for num in array:
        if vote_count == 0:
            candidate = num

        if num == candidate:
            vote_count += 1
        else:
            vote_count -= 1

    if array.count(candidate) > len(array) // 2:
        return candidate

    return None


# Test case 01
nums = [2, 2, 1, 1, 1, 2, 2, 1, 1, 3, 1, 1, 1]
print(majority_element(nums))