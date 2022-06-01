#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-06-01 16:55:44
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-06-01 19:51:27
FilePath: \LeetCode\473.火柴拼正方形.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=473 lang=python3
#
# [473] 火柴拼正方形
#

# @lc code=start


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalLen = sum(matchsticks)
        if totalLen % 4:
            return False
        matchsticks.sort(reverse=True)

        edges = [0] * 4

        def dfs(idx: int) -> bool:
            if idx == len(matchsticks):
                return True
            for i in range(4):
                edges[i] += matchsticks[idx]
                if edges[i] <= totalLen // 4 and dfs(idx + 1):
                    return True
                edges[i] -= matchsticks[idx]
            return False
        return dfs(0)
# @lc code=end
