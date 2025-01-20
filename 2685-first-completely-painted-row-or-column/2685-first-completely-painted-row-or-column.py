class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        ROWS,COLS = len(mat),len(mat[0])

        mov_to_pos = {}
        for r in range(ROWS):
            for c in range(COLS):
                mov_to_pos[mat[r][c]] = (r,c)

        row_cnt = [0] * ROWS
        col_cnt = [0] * COLS

        for i in range(len(arr)):
            r,c = mov_to_pos[arr[i]]

            row_cnt[r] += 1
            col_cnt[c] += 1

            if row_cnt[r] == COLS or col_cnt[c] == ROWS:
                return i
