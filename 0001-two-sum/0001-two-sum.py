class Solution:
    def twoSum(self, nums: List, target: int) :
        prevmap = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevmap:
                return (prevmap[diff],i)
            prevmap[n] = i
        return