class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def find(node):
            while circles[node] != node:
                circles[node] = circles[circles[node]]
                node = circles[node]
            return circles[node]
        
        n = len(M)
        circles = {x:x for x in range(n)}
        
        for i in range(n):
            for j in range(i, n):
                if i != j and M[i][j] == 1 and find(i) != find(j):
                    circles[find(i)] = find(j)   
                    
        return sum([1 for k, v in circles.items() if k == v])
        