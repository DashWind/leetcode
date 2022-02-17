# =========================================================================
# -*- coding: utf-8 -*-
# @Author  :   Neil Zhang
# @Time    :   2022/2/14 10:21
# @Desc    :   
# =========================================================================
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map_dict = {']': '[', '}': '{', ')': '('}
        queue = []

        for ch in s:
            if ch not in map_dict:
                queue.append(ch)
            else:
                if queue and queue[-1] == map_dict[ch]:
                    queue.pop()
                else:
                    return False
        return True