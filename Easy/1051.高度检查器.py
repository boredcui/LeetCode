#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-06-13 18:20:38
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-06-13 18:21:33
FilePath: \LeetCode\1051.高度检查器.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1051 lang=python3
#
# [1051] 高度检查器
#

# @lc code=start


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        return sum(1 for x, y in zip(heights, expected) if x != y)


# @lc code=end
