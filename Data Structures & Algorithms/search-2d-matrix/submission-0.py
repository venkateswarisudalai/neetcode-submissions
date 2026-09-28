class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        left = 0
        right = rows * columns -1
        if not matrix or not matrix[0]:
            return False
        while(left<=right):
            mid = (left+right)//2

            row = mid // columns
            column = mid % columns

            if matrix[row][column] == target:
                return True

            elif matrix[row][column] < target:
                left = mid+1
            
            else: 
                right = mid-1

        return False


        