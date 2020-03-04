class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        if k > len(nums):
            return False
        
        curr_sum = sum(nums)
        if curr_sum % k != 0:
            return False
        target = [curr_sum // k] * k
        
        nums.sort(reverse = True)
        
        def dfs(index = 0):
            if index == len(nums):
                return True
            
            for i in range(k):
                if nums[index] <= target[i]:
                    target[i] -= nums[index]
                    if dfs(index + 1):
                        return True
                    target[i] += nums[index]
            return False
        return dfs()