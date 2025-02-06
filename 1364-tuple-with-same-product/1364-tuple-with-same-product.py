class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prod_map = defaultdict(int)
        n = len(nums)

        for i in range(n):
            for j in range(i+1,n):
                product = nums[i] * nums[j]
                prod_map[product] += 1

        count = 0
        for k in prod_map.values():
            if k > 1:
                count += 8 *(k * (k-1)//2)
        return count