#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-05-12 13:41:07
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-05-12 13:53:36
FilePath: \LeetCode\944.删列造序.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=944 lang=python3
#
# [944] 删列造序
#

# @lc code=start


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(list(col) != sorted(col) for col in zip(*strs))
# @lc code=end
