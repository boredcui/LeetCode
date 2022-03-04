'''
Author: Boredcui
Date: 2022-03-04 12:44:32
LastEditors: Boredcui
LastEditTime: 2022-03-04 13:16:58
FilePath: \LeetCode\2104.子数组范围和.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2104 lang=python3
#
# [2104] 子数组范围和
#

# @lc code=start


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            maxVal, minVal = -inf, inf
            for j in range(i, n):
                maxVal = max(maxVal, nums[j])
                minVal = min(minVal, nums[j])
                ans += maxVal-minVal
        return ans
        # @lc code=end
