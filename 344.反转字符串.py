'''
Author: Boredcui
Date: 2022-03-01 12:56:56
LastEditors: Boredcui
LastEditTime: 2022-03-01 13:12:42
FilePath: \LeetCode\344.反转字符串.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        pos, rk = 0, n-1
        while pos < rk:
            s[pos], s[rk] = s[rk], s[pos]
            pos += 1
            rk -= 1
# @lc code=end
