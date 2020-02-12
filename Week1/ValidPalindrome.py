class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if not s:
            return True
        
        s = "".join( [ cha.lower() for cha in s if cha.isalnum() ])
        return s == s[::-1]