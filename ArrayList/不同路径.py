# =========================================================================
# -*- coding: utf-8 -*-
# @Author  :   Neil Zhang
# @Time    :   2022/2/16 13:39
# @Desc    :   
# =========================================================================
class Solution:

    def unique_paths_with_obstacles(self, obstacle_grid):
        n, m = len(obstacle_grid), len(obstacle_grid[0])
        f = [0] * m

        f[0] = 0 if obstacle_grid[0][0] else 1
        for i in range(n):
            for j in range(m):
                if obstacle_grid[i][j] == 1:
                    f[j] = 0
                    continue
                if j - 1 >= 0 and obstacle_grid[i][j - 1] == 0:
                    f[j] += f[j - 1]
        return f[m - 1]


print(Solution().unique_paths_with_obstacles([[0,0,0],[0,0,0],[0,0,0], [0, 0, 0]]))