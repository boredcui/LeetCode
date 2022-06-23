#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-06-23 23:47:03
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-06-23 23:47:13
FilePath: \LeetCode\30.串联所有单词的子串.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        return [
            i for i in range(len(s) - len(words) * len(words[0]) + 1)
            if Counter(
                s[j: j + len(words[0])]
                for j in range(i, i + len(words) * len(words[0]), len(words[0]))
            ) == Counter(words)
        ]
# @lc code=end
