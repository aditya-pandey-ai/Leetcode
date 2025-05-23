from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        seen = set()
        
        for row in matrix:
            for value in row:
                seen.add(value)
        
        return target in seen
