class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if n == 0:
            return 1
        elif n == -1:
            return 1/x
        
        curr_pow = self.myPow(x, n//2)
        
        return curr_pow*curr_pow if (n % 2) == 0 else curr_pow*curr_pow*x
        