class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        
        curr_index=0
        for mys in s:
            if mys not in t[curr_index:]:
                return False
            curr_index += t[curr_index:].index(mys) + 1
        return True