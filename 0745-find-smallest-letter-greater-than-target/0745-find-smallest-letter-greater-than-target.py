from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start, end = 0, len(letters) - 1

        while start <= end:
            mid = (start + end) // 2
            
            if letters[mid] <= target:  # Move right if `mid` is not greater than target
                start = mid + 1
            else:  # Move left if `mid` is greater
                end = mid - 1
        
        # If `start` moves beyond the last index, return first element (circular behavior)
        return letters[start % len(letters)]
