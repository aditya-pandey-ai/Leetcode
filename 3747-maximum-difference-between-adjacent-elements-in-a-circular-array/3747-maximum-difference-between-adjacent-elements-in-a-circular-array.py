from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = 0

        for i in range(n):
            # Circular next element using modulo
            next_i = (i + 1) % n
            curMax = abs(nums[i] - nums[next_i])
            maxi = max(maxi, curMax)

        return maxi
