class Solution:
    def minimumLength(self, s: str) -> int:
        freq_map = Counter(s)

        delete_count = 0
        for f in freq_map.values():
            if f % 2 == 1:
                delete_count += f - 1 
            else:
                delete_count += f - 2

        return len(s) - delete_count
