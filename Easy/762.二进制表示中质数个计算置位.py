'''
Author: Boredcui
Date: 2022-04-05 19:16:36
LastEditors: Boredcui
LastEditTime: 2022-04-05 19:16:51
FilePath: \LeetCode\762.二进制表示中质数个计算置位.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=762 lang=python3
#
# [762] 二进制表示中质数个计算置位
#


class Solution:
    def isPrime(self, x: int) -> bool:
        if x < 2:
            return False
        i = 2
        while i * i <= x:
            if x % i == 0:
                return False
            i += 1
        return True

    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum(self.isPrime(x.bit_count()) for x in range(left, right + 1))
# @lc code=end
