class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])

        def dfs(row,column,index):
            if row<0 or row>=rows or column<0 or column>=columns:
                return False

            if board[row][column] != word[index]:
                return False

            if index == len(word)-1:
                return True

            


            letter = board[row][column]
            board[row][column] = "#"

            found = (dfs(row+1,column,index+1) or dfs(row-1,column,index+1) or dfs(row,column+1,index+1) or dfs(row,column-1,index+1))
            board[row][column] = letter
            return found



        for i in range(rows):
            for j in range(columns):
                if dfs(i,j,0):
                    return True


        return False