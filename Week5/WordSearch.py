class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        def dfs(curr_board, i, j, word, index = 0):
            if index == len(word):
                return True
            
            if i < 0 or j < 0 or i >= len(curr_board) or j >= len(curr_board[0]) or curr_board[i][j] != word[index]:
                return False
            
            curr_board[i][j] = "#"
            
            curr =  dfs(curr_board, i-1, j, word, index + 1) or dfs(curr_board, i, j-1, word, index + 1) or dfs(curr_board, i+1, j, word, index + 1) or dfs(curr_board, i, j+1, word, index + 1)       
            
            return curr
        
           
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j] and dfs(board, i, j, word):
                    return True
                        
        return False
        