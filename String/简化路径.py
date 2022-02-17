# =========================================================================
# -*- coding: utf-8 -*-
# @Author  :   Neil Zhang
# @Time    :   2022/2/17 08:45
# @Desc    :   
# =========================================================================

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        names = path.split('/')
        stack = list()
        for name in names:
            if name == '..':
                if stack:
                    stack.pop()
            elif name and name != '.':
                stack.append(name)
        return '/' + '/'.join(stack)




