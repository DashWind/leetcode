# =========================================================================
# -*- coding: utf-8 -*-
# @Author  :   Neil Zhang
# @Time    :   2022/2/16 14:38
# @Desc    :   
# =========================================================================
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        dp = [0] * m
        dp[0] = grid[0][0]
        for i in range(n):
            for j in range(m):
                if i == 0:
                    if j > 0:
                        dp[j] = dp[j - 1] + grid[i][j]
                elif j == 0:
                    dp[j] += grid[i][j]
                else:
                    dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
        return dp[-1]


Solution().minPathSum([[1]])
