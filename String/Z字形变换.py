# =========================================================================
# -*- coding: utf-8 -*-
# @Author  :   Neil Zhang
# @Time    :   2022/2/14 08:28
# @Desc    :   按行排序
# =========================================================================


class Solution:

    def convert(self, s, num_rows):
        if num_rows == 1:
            return s

        rows = list()

        for i in range(min(len(s), num_rows)):
            rows.append('')

        cur_row = 0
        going_down = False

        for ch in s:
            rows[cur_row] += ch
            if cur_row == 0 or cur_row == num_rows - 1:
                going_down = not going_down
            cur_row += 1 if going_down else -1

        ret = ''
        for row in rows:
            ret += row
        return ret


a = 'PAYPALISHIRING'
result = Solution().convert(a, 3)
print(result)
