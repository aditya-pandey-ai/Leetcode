class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        frz = False
        fcz = False

        for i in range(cols):
            if matrix[0][i] == 0:
                frz = True
                break
        
        for i in range(rows):
            if matrix[i][0] == 0:
                fcz = True
                break
        
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0 
        
        if frz:
            for i in range(cols):
                matrix[0][i] = 0

        if fcz:
            for i in range(rows):
                matrix[i][0] = 0

        return matrix


