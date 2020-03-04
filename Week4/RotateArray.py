class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        k %= len(nums)
        
        while k != 0:
            nums.insert(i, nums[-k])
            del nums[-k]
            k -= 1
            i += 1
            
            
       