# =========================================================================
# -*- coding: utf-8 -*-
# @Author  :   Neil Zhang
# @Time    :   2022/2/16 16:22
# @Desc    :   
# =========================================================================
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) > len(b):
            b = (len(a) - len(b)) * '0' + b
        else:
            a = (len(b) - len(a)) * '0' + a

        c, val = '', 0
        for i in range(len(a) - 1, -1, -1):
            temp = int(a[i]) + int(b[i]) + val
            val = 0
            if int(temp) == 2:
                temp = 0
                val = 1
            c = str(temp) + c

        return str(val) + c if val else c

    def add_binary(self, a, b):
        x, y = int(a, 2), int(b, 2)
        # while y:
        #     answer = x ^ y
        #     carry = (x & y) << 1
        #     x, y = answer, carry
        x = x + y
        return bin(x)[2:]

print(Solution().add_binary('1111', '1111'))
