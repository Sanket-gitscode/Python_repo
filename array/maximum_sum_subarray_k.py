def maximum_sum_subarray_window_size(array: list[int], window_size: int):

    if not array or window_size <= 0 or window_size > len(array):
        return None
    
    # Sum of the first window
    current_window_sum = sum(array[:window_size])
    max_sum = current_window_sum
    best_start_window = 0

    # Slide the window
    for i in range(window_size, len(array)):
        current_window_sum = current_window_sum - array[i - window_size] + array[i] 

        if current_window_sum > max_sum:
            max_sum = current_window_sum
            best_start_window = i - window_size + 1

    return max_sum, array[best_start_window:best_start_window + window_size]


# Test case
arr = [2, 1, 5, 1, 3, 2]
window_size = 3

print(maximum_sum_subarray_window_size(arr,window_size))