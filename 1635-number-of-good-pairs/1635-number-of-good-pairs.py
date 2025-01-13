class Solution:
    def numIdenticalPairs(self, nums):
        count = defaultdict(int)
        res = 0

        for n in nums:
            if n in count:
                res += count[n]
                count[n] += 1
            else:
                count[n] = 1
        return res

