'''
Author: Boredcui
Date: 2022-03-01 19:17:31
LastEditors: Boredcui
LastEditTime: 2022-03-01 19:50:08
FilePath: \LeetCode\20.有效的括号.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashs = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i not in hashs:
                stack.append(i)
            if i in hashs:
                if stack and hashs[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack


# @lc code=end
