from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        my_counter = Counter(s)
        for i, char in enumerate(s):
            if my_counter[char] == 1:
                return i
            
        return -1
        
            
        