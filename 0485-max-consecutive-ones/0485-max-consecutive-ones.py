class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxcnt = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                maxcnt = max(maxcnt,count)
                count = 0
        
        return max(count,maxcnt)