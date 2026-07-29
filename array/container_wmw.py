#container with most water 

def maxArea_bruteforce(height):
        n = len(height)
        max_water = 0

        for i in range(n):
            for j in range(i + 1, n):
                width = j - i
                h = min(height[i], height[j])
                area = width * h
                max_water = max(max_water, area)

        return max_water


def maxArea_two_optimal(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        area = width * h

        max_water = max(max_water, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


height = [1,8,6,2,5,4,8,3,7]
print(maxArea_bruteforce(height))
print(maxArea_two_optimal(height))