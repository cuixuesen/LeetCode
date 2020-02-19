class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        
        
        res = []
        
        def dfs(curr_board, i, j, word, index = 0):
            if index == len(word):
                return True
            
            if i < 0 or j < 0 or i >= len(curr_board) or j >= len(curr_board[0]) or curr_board[i][j] != word[index]:
                return False
            
            curr_board[i][j], temp = "#", curr_board[i][j]
            
            curr =  dfs(curr_board, i-1, j, word, index + 1) or dfs(curr_board, i, j-1, word, index + 1) or dfs(curr_board, i+1, j, word, index + 1) or dfs(curr_board, i, j+1, word, index + 1)
                    
            curr_board[i][j] = temp
            return curr
        
           
        for i in range(len(board)):
            for j in range(len(board[0])):
                for word in words:
                    if word not in res and word[0] == board[i][j] and dfs(board[:][:], i, j, word):
                        res.append(word)
                        
        return res
        """
        trie={}
        for w in words:
            t=trie
            for c in w:
                if c not in t:
                    t[c]={}
                t=t[c]
            t['#']='#'
        self.res=set()
        self.used=[[False]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.find(board,i,j,trie,'')
        return list(self.res)
    
    def find(self,board,i,j,trie,pre):
        if '#' in trie:
            self.res.add(pre)
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
            return
        if not self.used[i][j] and board[i][j] in trie:
            self.used[i][j]=True
            self.find(board,i+1,j,trie[board[i][j]],pre+board[i][j])
            self.find(board,i,j+1,trie[board[i][j]],pre+board[i][j])
            self.find(board,i-1,j,trie[board[i][j]],pre+board[i][j])
            self.find(board,i,j-1,trie[board[i][j]],pre+board[i][j])
            self.used[i][j]=False
            
        
    
        
        
        
                        
                        
                            