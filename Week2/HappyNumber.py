class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        myDict = []
        while n not in myDict:
            myDict.append(n)
            n = str(n)
            result = 0
            for item in n:
                result += int(item)**2
            n = result
        return n == 1