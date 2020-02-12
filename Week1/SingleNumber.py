class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        return_result = 0
        
        for number in nums:
            return_result ^= number
        
        
        return return_result