#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-06-09 21:38:56
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-06-09 21:39:11
FilePath: \LeetCode\497.非重叠矩形中的随机点.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=497 lang=python3
#
# [497] 非重叠矩形中的随机点
#

# @lc code=start


class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.sum = [0]
        for a, b, x, y in rects:
            self.sum.append(self.sum[-1] + (x - a + 1) * (y - b + 1))

    def pick(self) -> List[int]:
        k = randrange(self.sum[-1])
        rectIndex = bisect_right(self.sum, k) - 1
        a, b, _, y = self.rects[rectIndex]
        da, db = divmod(k - self.sum[rectIndex], y - b + 1)
        return [a + da, b + db]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
# @lc code=end
