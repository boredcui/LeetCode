#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-05-08 15:36:21
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-05-08 15:52:48
FilePath: \LeetCode\442.数组中重复的数据.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=442 lang=python3
#
# [442] 数组中重复的数据
#

# @lc code=start


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            x = abs(x)
            if nums[x - 1] > 0:
                nums[x - 1] = -nums[x - 1]
            else:
                ans.append(x)
        return ans
# @lc code=end
