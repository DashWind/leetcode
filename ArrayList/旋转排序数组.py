# =========================================================================
# -*- coding: utf-8 -*-
# @Author  :   Neil Zhang
# @Time    :   2022/2/14 16:52
# @Desc    :   
# =========================================================================
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] < target < nums[mid]:
                r = mid - 1
            elif nums[mid] < target < nums[r]:
                l = mid + 1
        return -1


print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
