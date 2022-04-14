'''
Author: Boredcui
Date: 2022-04-14 13:09:36
LastEditors: Boredcui
LastEditTime: 2022-04-14 13:09:54
FilePath: \LeetCode\1672.最富有客户的资产总量.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1672 lang=python3
#
# [1672] 最富有客户的资产总量
#

# @lc code=start


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))
# @lc code=end
