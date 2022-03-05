'''
Author: Boredcui
Date: 2022-03-05 14:13:12
LastEditors: Boredcui
LastEditTime: 2022-03-05 14:22:07
FilePath: \LeetCode\521.最长特殊序列-ⅰ.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=521 lang=python3
#
# [521] 最长特殊序列 Ⅰ
#

# @lc code=start


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return max(len(a), len(b))if a != b else -1
# @lc code=end
