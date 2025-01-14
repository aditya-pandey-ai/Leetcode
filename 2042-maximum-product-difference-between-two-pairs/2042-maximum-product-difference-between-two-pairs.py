class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
            nums.sort()
            lowest = nums[0] * nums[1]
            highest = nums[-1] * nums[-2]
            return highest - lowest