'''
Author: Boredcui
Date: 2022-03-01 18:24:38
LastEditors: Boredcui
LastEditTime: 2022-03-01 18:34:17
FilePath: \LeetCode\1137.第-n-个泰波那契数.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1137 lang=python3
#
# [1137] 第 N 个泰波那契数
#

# @lc code=start


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        a, b, c = 0, 1, 1
        for i in range(2, n):
            a, b, c = (b, c, a+b+c)
        return c
# @lc code=end
