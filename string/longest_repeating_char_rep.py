#longest repeatting character replacement  AABA  -> AAAA if k = 1 meaning you can replace one character 
def longest_repeating_char_replacement(string: str, k: int):

    left = 0
    max_freq = 0
    max_len = 0
    count = {}

    for right in range(len(string)):

        count[string[right]] = count.get(string[right], 0) + 1

        max_freq = max(max_freq, count[string[right]])

        while (right - left + 1) - max_freq > k:
            count[string[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


print(longest_repeating_char_replacement("AAABABAA", 1))