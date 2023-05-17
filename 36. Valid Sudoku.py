from typing import List

class Solution:
    def checkRowsAndColumns(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rowElements = set()
            columnElements = set()
            for j in range(9):
                if board[i][j] == '.':
                    pass
                elif board[i][j] not in rowElements:
                    rowElements.add(board[i][j])
                else:
                    return False
                if board[j][i] == '.':
                    pass
                elif board[j][i] not in columnElements:
                    columnElements.add(board[j][i])
                else:
                    return False
        return True
    
    def checkQuadrant(self, board: List[List[str]], row: int, col: int) -> bool:
        quadrantElements = set()
        for i in range(row, row+3):
            for j in range(col, col+3):
                if board[i][j] == '.':
                    continue
                elif board[i][j] not in quadrantElements:
                    quadrantElements.add(board[i][j])
                else:
                    return False
        return True


    def checkQuadrants(self, board: List[List[str]]) -> bool:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if self.checkQuadrant(board, i, j) == False:
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        isValid = self.checkRowsAndColumns(board)
        isValid = isValid and self.checkQuadrants(board)
        return isValid

    
s = Solution()
isValid = s.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])

print(isValid)

isValid2 = s.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])

print(isValid2)