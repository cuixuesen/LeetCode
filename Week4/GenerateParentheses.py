class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n < 1:
            return []
        return_result = []
        
        def generateParenthesis_helper(curr_str="(", left=1, right=0):
            if len(curr_str) == 2*n:
                return_result.append(curr_str)
                return
            if left < n:
                generateParenthesis_helper(curr_str + '(', left+1, right)
            if right < left:
                generateParenthesis_helper(curr_str + ')', left, right+1)
            
        generateParenthesis_helper()
        
        return return_result