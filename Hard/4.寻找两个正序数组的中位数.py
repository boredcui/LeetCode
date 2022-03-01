'''
Author: Boredcui
Date: 2022-02-27 13:14:00
LastEditors: Boredcui
LastEditTime: 2022-02-27 14:10:34
FilePath: \LeetCode\4.寻找两个正序数组的中位数.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        ans = [0]*(n+m)
        i, j, pos = 0, 0, 0
        while pos < (m+n):
            if i == n:
                ans[pos] = nums2[j]
                pos += 1
                j += 1
                continue
            elif j == m:
                ans[pos] = nums1[i]
                pos += 1
                i += 1
                continue
            elif nums1[i] < nums2[j]:
                ans[pos] = nums1[i]
                pos += 1
                i += 1
                continue
            elif nums1[i] > nums2[j]:
                ans[pos] = nums2[j]
                pos += 1
                j += 1
                continue
            elif nums1[i] == nums2[j]:
                ans[pos] = nums1[i]
                ans[pos+1] = nums2[j]
                pos += 2
                i += 1
                j += 1
                continue
        if (m+n) % 2 == 0:
            return (ans[(m+n)//2-1]+ans[(m+n)//2])/2
        else:
            return ans[(m+n)//2]
# @lc code=end
