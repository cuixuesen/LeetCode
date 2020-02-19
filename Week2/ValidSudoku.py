class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        row = [[] for _ in range(9)]
        box = [[] for _ in range(9)]
        column = [[] for _ in range(9)]
        
        
        for i in reversed(range(9)):
            for j in reversed(range(9)):
                if board[i][j] != ".":
                    
                    box_index = (i//3)*3 + j//3
                    
                    if board[i][j] in row[i]:
                        return False
                    else:
                        row[i].append(board[i][j])
                    
                    if board[i][j] in column[j]:
                        return False
                    else:
                        column[j].append(board[i][j])
                        
                    if board[i][j] in box[box_index]:
                        return False
                    else:
                        box[box_index].append(board[i][j])       

        return True