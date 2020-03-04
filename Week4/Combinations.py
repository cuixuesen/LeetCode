class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        
        def combine_helper(curr_list = [], start = 1):
            if len(curr_list) == k:
                return_result.append(curr_list[:])
                return
            
            for i in range(start, n + 1):
                if my_list[i] == 1:
                    curr_list.append(i)
                    my_list[i] = 0
                    combine_helper(curr_list, i)
                    curr_list.pop()
                    my_list[i] = 1
        
        my_list = [1] * (n + 1)
        return_result = []
        combine_helper()
        return return_result
        