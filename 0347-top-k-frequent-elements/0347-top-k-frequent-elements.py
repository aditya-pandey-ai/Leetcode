class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = Counter(nums)  # Count occurrences
        return [key for key, _ in sorted(ctr.items(), key=lambda x: x[1], reverse=True)[:k]]  