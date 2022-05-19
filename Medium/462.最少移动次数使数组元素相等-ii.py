#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-05-19 21:54:10
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-05-19 21:59:39
FilePath: \LeetCode\462.最少移动次数使数组元素相等-ii.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=462 lang=python3
#
# [462] 最少移动次数使数组元素相等 II
#

# @lc code=start


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        return sum(abs(num - nums[len(nums) // 2]) for num in nums)
# @lc code=end
