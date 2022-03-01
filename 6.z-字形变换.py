'''
Author: Boredcui
Date: 2022-03-01 08:53:58
LastEditors: Boredcui
LastEditTime: 2022-03-01 12:54:04
FilePath: \LeetCode\6.z-字形变换.py
Description:

Copyright (c) 2022 by boredcui, All Rights Reserved.
'''
#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return "".join(res)
# @lc code=end
