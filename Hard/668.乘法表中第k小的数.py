#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-05-18 20:21:22
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-05-18 20:37:52
FilePath: \LeetCode\668.乘法表中第k小的数.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=668 lang=python3
#
# [668] 乘法表中第k小的数
#

# @lc code=start


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        return bisect_left(range(m * n), k, key=lambda x: x // n * n + sum(x // i for i in range(x // n + 1, m + 1)))

# @lc code=end
