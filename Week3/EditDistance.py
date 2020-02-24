class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        if not word1 or not word2:
            return max(len(word1), len(word2))
        
        dp = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]
        
        for i in range(len(word2)+1):
            for j in range(len(word1)+1):
                if i == 0 or j == 0:
                    dp[i][j] = max(i,j)
                    dp[0][0] = 0
         
        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
        return dp[-1][-1]
                
        
        