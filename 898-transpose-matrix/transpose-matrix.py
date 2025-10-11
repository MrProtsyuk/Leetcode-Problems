class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        return [[matrix[i][j] for i in range(rows)] for j in range(cols)]