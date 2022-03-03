'''
Author: Boredcui
Date: 2022-03-03 16:00:15
LastEditors: Boredcui
LastEditTime: 2022-03-03 17:42:50
FilePath: \LeetCode\567.字符串的排列.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
        dic1, dic2 = [0]*26, [0]*26
        for i in range(m):
            dic1[ord(s1[i])-ord('a')] += 1
            dic2[ord(s2[i])-ord('a')] += 1
        if dic1 == dic2:
            return True
        for i in range(m, n):
            dic2[ord(s2[i-m])-ord('a')] -= 1
            dic2[ord(s2[i])-ord('a')] += 1
            if dic1 == dic2:
                return True
        return False
# @lc code=end
