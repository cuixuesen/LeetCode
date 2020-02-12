class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        
        def dfs(i,j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != "O":
                return 0
            
            board[i][j] = "W"
            
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i,j+1)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or j == 0 or i == (len(board) - 1) or j == (len(board[0]) - 1):
                    if board[i][j] == "O":
                        dfs(i,j)
        
        mapping = {"X":"X", "O":"X", "W":"O"}
        for i in range(len(board)):
            for j in range(len(board[0])):       
                board[i][j] = mapping[board[i][j]]
        