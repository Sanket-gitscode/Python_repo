def maxWindow(arr, k):
    left = 0
    current_sum = 0

    maxLen = 0
    best_left = 0
    best_right = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum > k:
            current_sum -= arr[left]
            left += 1

        if right - left + 1 > maxLen:
            maxLen = right - left + 1
            best_left = left
            best_right = right

    return maxLen, arr[best_left:best_right + 1]

arr = [2, 1, 3, 4, 2]
print(maxWindow(arr, 7))