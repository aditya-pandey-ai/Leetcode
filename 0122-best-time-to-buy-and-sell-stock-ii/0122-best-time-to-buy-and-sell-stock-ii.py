class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0

        for i in range(len(prices) - 1):
            if prices[i] < prices[i+1]:
                mp += prices[i+1] - prices[i]
            else:
                mp += 0
        return mp