class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def bin(row):
            start = 0
            end = len(row) - 1

            while(start <= end):
                mid = (start+end)//2

                if row[mid] < 0:
                    end = mid - 1
                else:
                    start = mid +1
            return len(row)-start

        count = 0
        for row in grid:
            count += bin(row)
        return count