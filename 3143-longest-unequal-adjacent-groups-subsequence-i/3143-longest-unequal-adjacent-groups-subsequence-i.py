class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = [words[0]]
        last_groups = groups[0]

        for i in range(1, len(words)):
            if groups[i] != last_groups:
                result.append(words[i])
                last_groups = groups[i]
        
        return result

