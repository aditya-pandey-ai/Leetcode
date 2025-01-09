class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        n = len(words)

        for i in range(n):
            str1 = words[i]

            if str1.startswith(pref):
                count += 1
        return count