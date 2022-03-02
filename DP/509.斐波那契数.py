'''
Author: Boredcui
Date: 2022-03-01 18:15:06
LastEditors: Boredcui
LastEditTime: 2022-03-01 18:23:47
FilePath: \LeetCode\509.斐波那契数.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start


class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        for _ in range(1, n):
            a, b = (b, a+b)
        return b
# @lc code=end
