class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        Increase,Decrease = True,True

        for i in range(len(nums)-1):
            if not (nums[i] <= nums [i+1]):
                Increase = False
            if not (nums[i] >= nums [i+1]):
                Decrease = False
        return Increase or Decrease