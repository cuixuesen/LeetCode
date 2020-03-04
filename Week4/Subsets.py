class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def subsets_helper(curr_str = [], start = 0):
            if len(curr_str) > length:
                return
            if len(curr_str) > 0:
                return_result.append(curr_str[:])
                
            for i in range(start, length):
                if nums[i] != "HI":
                    curr_str.append(nums[i])
                    temp = nums[i]
                    nums[i] = "HI"
                    subsets_helper(curr_str,i)
                    curr_str.pop()
                    nums[i] = temp
                
        return_result = [[]]
        length = len(nums)
        subsets_helper()
        return return_result