#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-07-05 23:19:25
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-07-05 23:19:50
FilePath: \LeetCode\729.我的日程安排表-i.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=729 lang=python3
#
# [729] 我的日程安排表 I
#

# @lc code=start


class MyCalendar:
    def __init__(self):
        self.booked = []

    def book(self, start: int, end: int) -> bool:
        if any(l < end and start < r for l, r in self.booked):
            return False
        self.booked.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end
