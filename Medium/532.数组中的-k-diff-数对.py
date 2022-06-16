#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-06-16 14:40:55
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-06-16 14:41:21
FilePath: \LeetCode\532.数组中的-k-diff-数对.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=532 lang=python3
#
# [532] 数组中的 k-diff 数对
#

# @lc code=start


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        visited, res = set(), set()
        for num in nums:
            if num - k in visited:
                res.add(num - k)
            if num + k in visited:
                res.add(num)
            visited.add(num)
        return len(res)

# @lc code=end
