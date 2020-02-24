class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        
        res, index = 0, 0
        
        for cookie in s:
            if g[index] <= cookie:
                res += 1
                index += 1
                if index >= len(g):
                    return res
            
        return res