#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-06-21 23:03:51
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-06-21 23:11:21
FilePath: \LeetCode\1108.ip-地址无效化.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1108 lang=python3
#
# [1108] IP 地址无效化
#

# @lc code=start
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


# @lc code=end
