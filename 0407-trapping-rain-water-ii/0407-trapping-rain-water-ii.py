class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ROWS, COLS = len(heightMap), len(heightMap[0])
        
        min_heap = []
        # Add all boundary cells to the heap
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
                    heappush(min_heap, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1  # Mark as visited

        res = 0
        max_h = 0

        # Process the heap
        while min_heap:
            h, r, c = heappop(min_heap)
            max_h = max(max_h, h)
            
            # Check all neighbors
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= nr < ROWS and 0 <= nc < COLS and heightMap[nr][nc] != -1:
                    res += max(0, max_h - heightMap[nr][nc])
                    heappush(min_heap, (heightMap[nr][nc], nr, nc))
                    heightMap[nr][nc] = -1  # Mark as visited
        
        return res