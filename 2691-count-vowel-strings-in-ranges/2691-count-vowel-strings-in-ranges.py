from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel_set = set("aeiou")

        # Compute prefix counts for words that start and end with vowels
        prev_cnt = [0] * (len(words) + 1)
        for i, w in enumerate(words):
            if w[0] in vowel_set and w[-1] in vowel_set:
                prev_cnt[i + 1] = prev_cnt[i] + 1
            else:
                prev_cnt[i + 1] = prev_cnt[i]

        # Process each query
        res = [0] * len(queries)
        for i, q in enumerate(queries):
            l, r = q
            res[i] = prev_cnt[r + 1] - prev_cnt[l]

        return res
