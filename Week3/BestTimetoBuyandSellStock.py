class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        curr_price, max_pro = float("inf"), 0
        
        for price in prices:
            curr_price = min(curr_price, price)
            max_pro = max(max_pro, price - curr_price)
            
        return max_pro