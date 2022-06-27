#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-06-27 18:47:12
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-06-27 18:47:41
FilePath: \LeetCode\522.最长特殊序列-ii.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=522 lang=python3
#
# [522] 最长特殊序列 II
#

# @lc code=start


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subseq(s: str, t: str) -> bool:
            pt_s = pt_t = 0
            while pt_s < len(s) and pt_t < len(t):
                if s[pt_s] == t[pt_t]:
                    pt_s += 1
                pt_t += 1
            return pt_s == len(s)

        ans = -1
        for i, s in enumerate(strs):
            check = True
            for j, t in enumerate(strs):
                if i != j and is_subseq(s, t):
                    check = False
                    break
            if check:
                ans = max(ans, len(s))

        return ans


# @lc code=end
