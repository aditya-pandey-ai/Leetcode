class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        return sum(len({*s[s.index(c)+1:s.rindex(c)]}) for c in {*s})