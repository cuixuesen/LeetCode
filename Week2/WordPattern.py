class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        pattern = list(pattern)
        
        if len(str) != len(pattern):
            return False
        
        return len(set(zip(pattern, str))) == len(set(pattern)) == len(set(str))
        
        