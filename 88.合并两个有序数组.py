'''
Author: Boredcui
Date: 2022-03-01 14:48:05
LastEditors: Boredcui
LastEditTime: 2022-03-01 14:57:25
FilePath: \LeetCode\88.合并两个有序数组.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos = 0
        for i in range(m, m+n):
            nums1[i] = nums2[pos]
            pos += 1
        nums1.sort()
# @lc code=end
