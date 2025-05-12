from collections import Counter
from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = Counter(digits)
        res = []

        for i in range(100, 1000, 2):  # Only even numbers
            d1, d2, d3 = i // 100, (i // 10) % 10, i % 10
            curr_freq = Counter([d1, d2, d3])

            if all(freq[d] >= curr_freq[d] for d in curr_freq):
                res.append(i)

        return res
