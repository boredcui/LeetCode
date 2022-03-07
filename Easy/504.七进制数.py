'''
Author: Boredcui
Date: 2022-03-07 13:59:41
LastEditors: Boredcui
LastEditTime: 2022-03-07 14:10:08
FilePath: \PythonCoursec:\Code\GitHub\LeetCode\504.七进制数.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        negative = num < 0
        num = abs(num)
        digits = []
        while num:
            digits.append(str(num % 7))
            num //= 7
        if negative:
            digits.append('-')
        return ''.join(reversed(digits))
# @lc code=end
