#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-05-06 20:19:20
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-05-06 21:19:49
FilePath: \LeetCode\933.最近的请求次数.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=933 lang=python3
#
# [933] 最近的请求次数
#

# @lc code=start


class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

        # Your RecentCounter object will be instantiated and called as such:
        # obj = RecentCounter()
        # param_1 = obj.ping(t)
        # @lc code=end
