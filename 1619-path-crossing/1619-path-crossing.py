class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dir = {
            'N': [0, 1],
            'S': [0, -1],
            'E': [1, 0],
            'W': [-1, 0]
        }

        visited = set()
        x,y = 0,0

        for p in path:
            visited.add((x,y))
            dx,dy = dir[p]
            x , y = dx + x, dy + y
            if (x,y) in visited:
                return True
        return False
