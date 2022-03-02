'''
Author: Boredcui
Date: 2022-03-02 12:26:43
LastEditors: Boredcui
LastEditTime: 2022-03-02 12:56:04
FilePath: \LeetCode\350.两个数组的交集-ii.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        len1, len2 = len(nums1), len(nums2)
        index1 = index2 = 0
        intersection = list()

        while index1 < len1 and index2 < len2:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                intersection.append(nums1[index1])
                index1 += 1
                index2 += 1
        return intersection
# @lc code=end
