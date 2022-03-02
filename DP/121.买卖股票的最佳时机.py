'''
Author: Boredcui
Date: 2022-03-02 12:56:43
LastEditors: Boredcui
LastEditTime: 2022-03-02 13:35:28
FilePath: \LeetCode\121.买卖股票的最佳时机.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = int(1e9)
        maxprofit = 0

        for price in prices:
            maxprofit = max(price-minprice, maxprofit)
            minprice = min(price, minprice)

        return maxprofit
# @lc code=end
