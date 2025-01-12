class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        Balloon = Counter("balloon")

        res = len(text)

        for c in Balloon:
            res = min(res, countText[c] // Balloon[c])
        return res