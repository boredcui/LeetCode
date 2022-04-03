'''
Author: Boredcui
Date: 2022-04-03 18:03:16
LastEditors: Boredcui
LastEditTime: 2022-04-03 18:03:37
FilePath: \LeetCode\744.寻找比目标字母大的最小字母.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=744 lang=python3
#
# [744] 寻找比目标字母大的最小字母
#

# @lc code=start


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[bisect_right(letters, target)] if target < letters[-1] else letters[0]
# @lc code=end
