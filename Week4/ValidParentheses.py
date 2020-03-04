class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        
        mapping = { "(":")", "{":"}", "[":"]" }
        
        for item in s:
            if item in mapping:
                stack.append(item)
            else:
                if not stack:
                    return False
                elif mapping[stack.pop()] != item:
                    return False
        
        return not stack
                
            