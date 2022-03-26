'''
Author: Boredcui
Date: 2022-03-26 20:10:26
LastEditors: Boredcui
LastEditTime: 2022-03-26 20:21:55
FilePath: \LeetCode\682.棒球比赛.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#

# @lc code=start


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stk = []
        for op in ops:
            match op:
                case 'C':
                    stk.pop()
                case 'D':
                    stk.append(stk[-1]*2)
                case '+':
                    stk.append(stk[-1]+stk[-2])
                case _:
                    stk.append(int(op))
        return sum(stk)
        # @lc code=end
