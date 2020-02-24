class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        
        points.sort(key = lambda x: x[1])
        
        arrow, first_end = 1, points[0][1]
        
        for start, end in points:
            if start > first_end:
                arrow +=1
                first_end = end
        
        return arrow