'''
Author: Boredcui
Date: 2022-03-03 13:43:13
LastEditors: Boredcui
LastEditTime: 2022-03-03 14:01:39
FilePath: \LeetCode\258.各位相加.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start


class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = num % 10+(num//10)
        return num
# @lc code=end
