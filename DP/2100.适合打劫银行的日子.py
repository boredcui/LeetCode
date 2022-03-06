'''
Author: Boredcui
Date: 2022-03-06 14:09:33
LastEditors: Boredcui
LastEditTime: 2022-03-06 14:33:47
FilePath: \LeetCode\2100.适合打劫银行的日子.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2100 lang=python3
#
# [2100] 适合打劫银行的日子
#

# @lc code=start


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        left, right = [0]*n, [0]*n
        for i in range(1, n):
            if security[i] <= security[i-1]:
                left[i] = left[i-1]+1
            if security[n-i-1] <= security[n-i]:
                right[n-i-1] = right[n-i]+1
        return [i for i in range(time, n-time) if left[i] >= time and right[i] >= time]
# @lc code=end
