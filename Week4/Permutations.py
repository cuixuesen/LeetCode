class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        def permute_helper(nums, curr_list = [], curr_index = 0):
            if len(curr_list) == len(nums):
                result.append(curr_list[:])
            else:
                for i in range(curr_index, len(nums)):
                    curr_list.append(nums[i])
                    permute_helper(nums, curr_list, i)
                    curr_list.pop()
            
        result = []
        permute_helper(nums)
        
        return result
        
        
        
        
        