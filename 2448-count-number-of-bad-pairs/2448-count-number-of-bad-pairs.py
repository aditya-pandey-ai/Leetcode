from collections import Counter

class Solution:
    def countBadPairs(self, nums):
        n = len(nums)
        total_pairs = n * (n - 1) // 2  # Total pairs
        
        key_freq = Counter()
        good_pairs = 0  # Count of good pairs
        
        for i, num in enumerate(nums):
            key = num - i
            good_pairs += key_freq[key]  # All previous occurrences of key form good pairs
            key_freq[key] += 1  # Update frequency of current key
        
        bad_pairs = total_pairs - good_pairs
        return bad_pairs
