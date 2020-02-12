class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        for item in A:
            for i in range(len(item)//2):
                item[i],item[-i -1] = item[-i -1], item[i]
            
            for i in range(len(item)):
                
                item[i] = 1 - item[i]
        return A
        