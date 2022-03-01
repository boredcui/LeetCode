'''
Author: Boredcui
Date: 2022-02-27 17:28:41
LastEditors: Boredcui
LastEditTime: 2022-02-27 17:51:34
FilePath: \LeetCode\11.盛最多水的容器.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = n-1
        pos = 0
        max = 0
        while pos <= i:
            if max < min(height[pos], height[i])*(i-pos):
                max = min(height[pos], height[i])*(i-pos)
            if height[pos] <= height[i]:
                pos += 1
                continue
            if height[pos] > height[i]:
                i -= 1
                continue
        return max
# @lc code=end
