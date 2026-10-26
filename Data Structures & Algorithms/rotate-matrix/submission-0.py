class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for row in range(n):
            for col in range(row+1,n):
                matrix[row][col],matrix[col][row] = matrix[col][row],matrix[row][col]

        
        for row in range(n):
            matrix[row].reverse()