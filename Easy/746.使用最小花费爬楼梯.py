'''
Author: Boredcui
Date: 2022-03-02 13:52:19
LastEditors: Boredcui
LastEditTime: 2022-03-02 14:05:38
FilePath: \LeetCode\746.使用最小花费爬楼梯.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0]*(n+1)
        for i in range(2, n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])

        return dp[n]

# @lc code=end
