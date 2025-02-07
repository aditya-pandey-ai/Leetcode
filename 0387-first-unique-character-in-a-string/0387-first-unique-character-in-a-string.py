class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        index = {}

        for pos,c in enumerate(s):
            count[c] += 1
            if c not in index:
                index[c] = pos
        
        for c in s:
            if count[c] == 1:
                return index[c]

        return -1