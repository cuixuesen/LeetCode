class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return_result = [0]
        for i in range(n):
            temp = []
            for curr in reversed(return_result):
                temp.append((2**i) + curr)
            return_result += temp
            
        return return_result