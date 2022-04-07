'''
Author: Boredcui
Date: 2022-04-07 14:59:58
LastEditors: Boredcui
LastEditTime: 2022-04-07 15:00:13
FilePath: \LeetCode\796.旋转字符串.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=796 lang=python3
#
# [796] 旋转字符串
#

# @lc code=start


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s
# @lc code=end
