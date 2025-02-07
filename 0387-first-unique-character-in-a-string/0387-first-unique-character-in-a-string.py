class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = Counter(s)
        for char in chars:
            if chars[char] == 1:
                return s.index(char)
        
        return -1