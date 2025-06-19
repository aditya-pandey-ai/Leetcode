class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        cnt = 0
        nums_s = sorted(nums)
        curr = nums_s[0]

        for n in nums_s:
            if (n - curr) > k:
                cnt += 1
                curr = n
        return cnt + 1