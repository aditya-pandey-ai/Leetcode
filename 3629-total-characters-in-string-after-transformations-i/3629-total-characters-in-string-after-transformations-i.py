class Solution:
    MOD = 10**9 + 7
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        freq = [0] * 26

        # Initialize frequencies from the input string
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Apply transformations t times
        for _ in range(t):
            new_freq = [0] * 26
            for i in range(26):
                if freq[i] == 0:
                    continue
                if i == 25:  # 'z'
                    new_freq[0] = (new_freq[0] + freq[i]) % self.MOD
                    new_freq[1] = (new_freq[1] + freq[i]) % self.MOD
                else:
                    new_freq[i + 1] = (new_freq[i + 1] + freq[i]) % self.MOD
            freq = new_freq

        return sum(freq) % self.MOD