class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if not s:
            return ""
        
        result = []
        prev = 0
        for i in range(len(s)):
            if s[i] == " ":
                prev = i + 1
            result.insert(prev,s[i])
        return "".join(result)
        