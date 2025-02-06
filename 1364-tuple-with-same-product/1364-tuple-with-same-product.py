class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prod_map = defaultdict(list)
        n = len(nums)

        for i in range(n):
            for j in range(i+1,n):
                product = nums[i] * nums[j]
                prod_map[product].append((nums[i],nums[j]))

        count = 0
        for pairs in prod_map.values():
            k = len(pairs)
            if k > 1:
                count += 8 *(k * (k-1)//2)
        return count