'''
Author: Boredcui
Date: 2022-03-02 13:36:36
LastEditors: Boredcui
LastEditTime: 2022-03-02 13:51:46
FilePath: \LeetCode\70.爬楼梯.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
# @lc code=end
