class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        l,r = 0,1
        maxP= -1 

        while r < len(nums):
            if nums[l] < nums[r]:
                profit = nums[r] - nums[l]
                maxP = max(maxP,profit)
            else:
                l = r
            r += 1
        return maxP