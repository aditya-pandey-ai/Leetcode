import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        h = []
        heapq.heapify(nums)
        while nums:
            h.append(heapq.heappop(nums))
        return h