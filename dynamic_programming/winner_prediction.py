from functools import lru_cache

def PredictTheWinner(nums):

    @lru_cache(None)
    def dp(i, j):

        # only one number left
        if i == j:
            return nums[i]

        # take left number
        take_left = nums[i] - dp(i + 1, j)

        # take right number
        take_right = nums[j] - dp(i, j - 1)

        # choose the better move
        return max(take_left, take_right)

    return dp(0, len(nums) - 1) >= 0

arr = [1,5,2]
print(PredictTheWinner(arr))