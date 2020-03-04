class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        hor, ver, nine = [[] for _ in range(9)], [[] for _ in range(9)], [[] for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    hor[i].append(int(board[i][j]))
                    ver[j].append(int(board[i][j]))
                    nine[(i//3)*3 + j//3].append(int(board[i][j]))
    
        
        def dfs(i = 0, j = 0):
            if j == 9:
                i += 1
                j = 0
                
            if i == 9:
                return True
            
            if board[i][j] != ".":
                return dfs(i, j + 1)
            
            for num in range(1,10):
                if num not in hor[i] and num not in ver[j] and num not in nine[(i//3)*3 + j//3]:
                    hor[i].append(num)
                    ver[j].append(num)
                    nine[(i//3)*3 + j//3].append(num)
                    board[i][j] = str(num)
                    if dfs(i, j+1):
                        return True
                    hor[i].remove(num)
                    ver[j].remove(num)
                    nine[(i//3)*3 + j//3].remove(num)
                    board[i][j] = "."
        
        dfs()
                    
            
        