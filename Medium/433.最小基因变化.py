#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-05-07 16:16:52
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-05-07 18:47:53
FilePath: \LeetCode\433.最小基因变化.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0
        bank = set(bank)
        if end not in bank:
            return -1
        q = deque([(start, 0)])
        while q:
            cur, step = q.popleft()
            for i, x in enumerate(cur):
                for y in "ACGT":
                    if y != x:
                        nxt = cur[:i] + y + cur[i + 1:]
                        if nxt in bank:
                            if nxt == end:
                                return step + 1
                            bank.remove(nxt)
                            q.append((nxt, step + 1))
        return -1
# @lc code=end
