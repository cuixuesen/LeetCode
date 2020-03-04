class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = target // 2
        
        dp = [[0 for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        
        dp[0][0] = 1
        
        for i in range(1, len(nums) + 1):
            for j in range(1, target+1):
                if j - nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]
        