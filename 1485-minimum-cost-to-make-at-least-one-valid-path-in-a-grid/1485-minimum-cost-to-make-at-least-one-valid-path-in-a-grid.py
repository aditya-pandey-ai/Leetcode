class Solution:
    def minCost(self, A):
        """
        Find minimum cost to create valid path in grid using hybrid DFS-BFS approach
        Args:
            A: 2D grid where each cell contains 1-4 representing directions
               1: right, 2: left, 3: down, 4: up
        Returns:
            int: minimum cost to create valid path to bottom-right
        """
        n, m = len(A), len(A[0])  # Grid dimensions
        inf = 10**9               # Infinity value
        k = 0                     # Current cost level
        
        # Initialize distance array with infinity
        dp = [[inf] * m for i in range(n)]
        
        # Possible directions: right, left, down, up
        dirt = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        # Queue for BFS
        bfs = []
        
        def dfs(x, y):
            # Check if position is valid and unvisited
            if not (0 <= x < n and 0 <= y < m and dp[x][y] == inf):
                return
                
            # Mark current cell with current cost level
            dp[x][y] = k
            bfs.append([x, y])
            
            # Follow the arrow direction using DFS
            next_x = x + dirt[A[x][y] - 1][0]
            next_y = y + dirt[A[x][y] - 1][1]
            dfs(next_x, next_y)
        
        # Start DFS from top-left corner
        dfs(0, 0)
        
        # BFS to handle cells that need changes
        while bfs:
            k += 1                    # Increment cost
            bfs, bfs2 = [], bfs      # Swap queues
            
            # Try all directions from each cell in current level
            for x, y in bfs2:
                for i, j in dirt:
                    dfs(x + i, y + j)
        
        return dp[-1][-1]            # Return cost at bottom-right