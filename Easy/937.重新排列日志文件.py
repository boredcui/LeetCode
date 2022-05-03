'''
Author: Boredcui
Date: 2022-05-03 14:59:50
LastEditors: Boredcui
LastEditTime: 2022-05-03 15:14:46
FilePath: \LeetCode\937.重新排列日志文件.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=937 lang=python3
#
# [937] 重新排列日志文件
#

# @lc code=start


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def trans(log: str) -> tuple:
            a, b = log.split(' ', 1)
            return (0, b, a) if b[0].isalpha() else (1,)

        logs.sort(key=trans)  # sort 是稳定排序
        return logs
# @lc code=end
