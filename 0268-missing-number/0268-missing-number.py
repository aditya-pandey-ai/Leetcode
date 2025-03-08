class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        
        # XOR all numbers from 0 to n
        for i in range(n + 1):
            ans ^= i
        
        # XOR all elements in the array
        for num in nums:
            ans ^= num
        
        return ans
