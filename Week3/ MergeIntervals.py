class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        return_result = []
        intervals.sort(key = lambda i : i[0])
        for interval in intervals:
            if not return_result or return_result[-1][1] < interval[0]:
                return_result.append(interval)
            else:
                return_result[-1][1] = max(return_result[-1][1], interval[1])
        return return_result
        