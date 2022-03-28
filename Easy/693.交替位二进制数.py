'''
Author: Boredcui
Date: 2022-03-28 14:01:53
LastEditors: Boredcui
LastEditTime: 2022-03-28 14:08:21
FilePath: \LeetCode\693.交替位二进制数.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#

# @lc code=start


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        str = '{:b}'.format(n)
        for i in range(len(str)-1):
            if str[i] == str[i+1]:
                return False
        return True
        # @lc code=end
