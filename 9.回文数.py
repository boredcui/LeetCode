'''
Author: Boredcui
Date: 2022-02-25 20:55:29
LastEditors: Boredcui
LastEditTime: 2022-02-25 21:22:27
FilePath: \LeetCode\9.回文数.py
Description:

Copyright (c) 2022 by boredcui, All Rights Reserved.
'''
#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start

# my solution
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         num = 0
#         y = x
#         while y != 0:
#             num = num*10
#             num = num + y % 10
#             y = y//10
#         if num == x:
#             return True
#         return False

# advance


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x % 10 == 0 and x != 0:
            return False
        num = 0
        while x > num:
            num = num*10+x % 10
            x = x//10
        if x == num or x == num//10:
            return True
        return False
        # @lc code=end
