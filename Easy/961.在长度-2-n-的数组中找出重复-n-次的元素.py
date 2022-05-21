#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-05-21 19:40:16
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-05-21 19:44:25
FilePath: \LeetCode\961.在长度-2-n-的数组中找出重复-n-次的元素.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=961 lang=python3
#
# [961] 在长度 2N 的数组中找出重复 N 次的元素
#

# @lc code=start


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        found = set()

        for num in nums:
            if num in found:
                return num
            found.add(num)

        # 不可能的情况
        return -1
# @lc code=end
