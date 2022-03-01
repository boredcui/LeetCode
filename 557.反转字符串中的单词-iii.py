'''
Author: Boredcui
Date: 2022-03-01 13:13:43
LastEditors: Boredcui
LastEditTime: 2022-03-01 14:46:05
FilePath: \LeetCode\557.反转字符串中的单词-iii.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(map(lambda x: x[::-1], s.split()))

# @lc code=end
