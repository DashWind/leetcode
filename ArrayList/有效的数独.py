# =========================================================================
# -*- coding: utf-8 -*-
# @Author  :   Neil Zhang
# @Time    :   2022/2/15 09:32
# @Desc    :   
# =========================================================================
class Solution:

    def is_valid_sudoku(self, board):
        rows = [[0] * 9 for _ in range(9)]
        columns = [[0] * 9 for _ in range(9)]
        subboxes = [[[0] * 9 for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != '.':
                    idx = int(c) - 1
                    rows[i][idx] += 1
                    columns[j][idx] += 1
                    subboxes[i // 3][j // 3][idx] += 1
                    if rows[i][idx] > 1 or columns[j][idx] > 1 or subboxes[i // 3][j // 3][idx] > 1:
                        return False
        return True


result = Solution().is_valid_sudoku([
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
])

print(result)
