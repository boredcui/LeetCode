#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-07-04 23:03:05
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-07-04 23:03:46
FilePath: \LeetCode\1200.最小绝对差.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1200 lang=python3
#
# [1200] 最小绝对差
#

# @lc code=start


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        arr.sort()

        best, ans = float('inf'), list()
        for i in range(n - 1):
            if (delta := arr[i + 1] - arr[i]) < best:
                best = delta
                ans = [[arr[i], arr[i + 1]]]
            elif delta == best:
                ans.append([arr[i], arr[i + 1]])

        return ans

# @lc code=end
