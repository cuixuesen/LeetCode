class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        def combinationSum_helper(curr_list=[], remain=target, start = 0):
            if remain < 0:
                return
            if remain == 0:
                return_result.append(curr_list[:])
            
            for i in range(start,length):
                curr_list.append(candidates[i])
                combinationSum_helper(curr_list, remain - candidates[i], i)
                curr_list.pop()
            
        length = len(candidates)
        return_result = []
        combinationSum_helper()
        return return_result