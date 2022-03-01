'''
Author: Boredcui
Date: 2022-02-26 16:10:19
LastEditors: Boredcui
LastEditTime: 2022-02-26 16:54:23
FilePath: \LeetCode\278.第一个错误的版本.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low <= high:
            mid = (high+low)//2
            if isBadVersion(mid):
                high = mid-1
            else:
                low = mid+1
        return low
# @lc code=end
