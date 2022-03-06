'''
Author: Boredcui
Date: 2022-03-06 15:45:13
LastEditors: Boredcui
LastEditTime: 2022-03-06 16:27:37
FilePath: \LeetCode\36.有效的数独.py
Description:

Copyright (c) 2022 by boredcui, All Rights Reserved.
'''
#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0]*9 for _ in range(9)]
        colums = [[0]*9 for _ in range(9)]
        subboxes = [[[0]*9 for _ in range(3)]for _ in range(3)]
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != '.':
                    c = int(c)-1
                    rows[i][c] += 1
                    colums[j][c] += 1
                    subboxes[int(i/3)][int(j/3)][c] += 1
                    if rows[i][c] > 1 or colums[j][c] > 1 or subboxes[int(i/3)][int(j/3)][c] > 1:
                        return False
        return True
# @lc code=end
