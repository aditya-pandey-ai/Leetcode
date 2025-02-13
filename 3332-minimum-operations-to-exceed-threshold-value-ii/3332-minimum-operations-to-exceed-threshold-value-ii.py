class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        heapify (nums)
        ans  = 0
        num = heappop(nums)
        
        while num < k:
            
            nxt = 2 * num+heappop(nums)
            num = heappushpop(nums, nxt)
            ans+= 1

        return ans