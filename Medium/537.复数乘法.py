'''
Author: Boredcui
Date: 2022-02-25 12:02:51
LastEditors: Boredcui
LastEditTime: 2022-02-25 18:31:18
FilePath: \LeetCode\537.复数乘法.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=537 lang=python3
#
# [537] 复数乘法
#

# @lc code=start


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, imag1 = map(int, num1[:-1].split('+'))
        real2, imag2 = map(int, num2[:-1].split('+'))
        return f'{real1*real2-imag1*imag2}+{real1*imag2+imag1*real2}i'
        # @lc code=end
