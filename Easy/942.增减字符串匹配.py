#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-05-09 17:00:28
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-05-09 17:20:04
FilePath: \LeetCode\942.增减字符串匹配.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=942 lang=python3
#
# [942] 增减字符串匹配
#

# @lc code=start


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        lo = 0
        hi = n = len(s)
        perm = [0] * (n + 1)
        for i, ch in enumerate(s):
            if ch == 'I':
                perm[i] = lo
                lo += 1
            else:
                perm[i] = hi
                hi -= 1
        perm[n] = lo  # 最后剩下一个数，此时 lo == hi
        return perm

# @lc code=end
