#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-06-12 22:13:07
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-06-12 22:13:40
FilePath: \LeetCode\890.查找和替换模式.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=890 lang=python3
#
# [890] 查找和替换模式
#

# @lc code=start


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word: str, pattern: str) -> bool:
            mp = {}
            for x, y in zip(word, pattern):
                if x not in mp:
                    mp[x] = y
                elif mp[x] != y:  # word 中的同一字母必须映射到 pattern 中的同一字母上
                    return False
            return True
        return [word for word in words if match(word, pattern) and match(pattern, word)]
# @lc code=end
