class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix),len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == target:
                    return True
        return False
        