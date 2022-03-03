'''
Author: Boredcui
Date: 2022-03-03 14:13:40
LastEditors: Boredcui
LastEditTime: 2022-03-03 14:45:46
FilePath: \LeetCode\566.重塑矩阵.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c:
            return mat
        nat = [[0] * c for _ in range(r)]
        for x in range(m*n):
            nat[x//c][x % c] = mat[x//n][x % n]
        return nat
# @lc code=end
