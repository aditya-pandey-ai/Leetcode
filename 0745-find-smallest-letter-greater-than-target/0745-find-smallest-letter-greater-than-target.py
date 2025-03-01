from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, h = 0, len(letters) - 1
        while l < h:
            mid = (h + l) // 2
            if letters[mid] > target:
                h = mid  # Move left to find a greater element
            else:
                l = mid + 1  # Move right if mid is <= target

        # Circular behavior: if no greater letter is found, return the first letter
        return letters[l] if letters[l] > target else letters[0]
