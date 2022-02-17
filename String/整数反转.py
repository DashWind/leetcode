# =========================================================================
# -*- coding: utf-8 -*-
# @Author  :   Neil Zhang
# @Time    :   2022/2/14 09:31
# @Desc    :   
# =========================================================================
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = - 2 ** 31, 2 ** 31 - 1
        ret = 0
        while x:
            if ret < INT_MIN or ret > INT_MAX:
                return 0

            digit = x % 10
            if x < 0 and digit > 0:
                digit -= 10

            x = (x - digit) // 10
            ret = ret * 10 + digit
        return ret


a = 1534236469
print(Solution().reverse(a))
