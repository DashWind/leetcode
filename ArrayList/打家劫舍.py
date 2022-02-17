# =========================================================================
# -*- coding: utf-8 -*-
# @Author  :   Neil Zhang
# @Time    :   2022/2/16 10:05
# @Desc    :   
# =========================================================================
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def rob_range(start, end):
            dp = [0, nums[start]]
            for i in range(start + 1, end):
                dp0 = max(dp[0], dp[1])
                dp1 = dp[0] + nums[i]
                dp = [dp0, dp1]
            return max(dp[0], dp[1])

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            return max(rob_range(0, len(nums) - 1), rob_range(1, len(nums)))


print(Solution().rob([1, 2, 3]))