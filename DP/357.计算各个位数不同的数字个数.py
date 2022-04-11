'''
Author: Boredcui
Date: 2022-04-11 10:26:58
LastEditors: Boredcui
LastEditTime: 2022-04-11 10:36:24
FilePath: \LeetCode\357.计算各个位数不同的数字个数.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=357 lang=python3
#
# [357] 计算各个位数不同的数字个数
#

# @lc code=start


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 10
        for i in range(2, n+1):
            dp[i] = dp[i-1]+(dp[i-1]-dp[i-2])*(10-(i-1))
        return dp[n]
        # @lc code=end
