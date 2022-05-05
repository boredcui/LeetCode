#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-05-05 16:16:30
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-05-05 19:00:34
FilePath: \LeetCode\713.乘积小于k的子数组.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于K的子数组
#

# @lc code=start


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans, prod, i = 0, 1, 0
        for j, num in enumerate(nums):
            prod *= num
            while i <= j and prod >= k:
                prod //= nums[i]
                i += 1
            ans += j - i + 1
        return ans
# @lc code=end
