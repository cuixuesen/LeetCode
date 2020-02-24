from collections import Counter
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last_index = { char:i for i, char in enumerate(S) }
        
        j, index, res = 0, 0, []
        
        for i, char in enumerate(S):
            j = max(j, last_index[char])
            if i == j:
                res.append(i - index + 1)
                index = i + 1     
                
        return res