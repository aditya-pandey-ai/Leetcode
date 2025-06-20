class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        x,y = 0,0
        res = 0
        move = 0

        for d in s:
            move += 1

            if d == "N":
                y +=1
            elif d == "S":
                y -= 1
            elif d == "W":
                x += 1
            else:
                x -= 1
        
            curr = abs(x) + abs(y)
            res = max(res, min(move, curr + (k * 2)))
        return res