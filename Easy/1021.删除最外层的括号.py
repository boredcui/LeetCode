#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-05-28 16:35:25
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-05-28 21:01:16
FilePath: \LeetCode\1021.删除最外层的括号.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#

# @lc code=start


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res, stack = "", []
        for c in s:
            if c == ')':
                stack.pop()
            if stack:
                res += c
            if c == '(':
                stack.append(c)
        return res
# @lc code=end
