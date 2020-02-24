class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def rob_helper(curr_nums):
            if not curr_nums:
                return 0
            
            dp = [0 for _ in range(len(curr_nums) + 1)]
            dp[1] = curr_nums[0]
        
            for i in range(2, len(curr_nums) + 1):
                dp[i] = max(dp[i-1], dp[i-2] + curr_nums[i-1])
            
            return dp[-1]
        
        if len(nums) == 1:
            return nums[0]
        return max(rob_helper(nums[:-1]), rob_helper(nums[1:]))
        