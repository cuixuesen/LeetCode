class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        index = {num:i for i,num in enumerate(nums2)}
        
        res = []
        
        for z, num in enumerate(nums1):
            for i in range(index[num] + 1, len(nums2)):
                if nums2[i] > num:
                    res.append(nums2[i])
                    break
            if z + 1 != len(res):
                res.append(-1)
                
        return res
        