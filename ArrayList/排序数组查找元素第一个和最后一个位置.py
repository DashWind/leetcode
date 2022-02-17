# =========================================================================
# -*- coding: utf-8 -*-
# @Author  :   Neil Zhang
# @Time    :   2022/2/15 08:31
# @Desc    :   
# =========================================================================

class Solution:

    def search_range(self, nums, target):
        left_idx = self.binary_search(nums, target, True)
        right_idx = self.binary_search(nums, target, False) - 1

        if left_idx <= right_idx < len(nums) and nums[left_idx] == target and nums[right_idx] == target:
            return [left_idx, right_idx]
        return [-1, -1]

    def binary_search(self, nums, target, lower):
        left, right, ans = 0, len(nums) - 1, len(nums),

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target or (lower and nums[mid] >= target):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans


print(Solution().search_range([5, 7, 7, 8, 8, 10], 8))
