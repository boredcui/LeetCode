'''
Author: Boredcui
Date: 2022-03-03 18:55:25
LastEditors: Boredcui
LastEditTime: 2022-03-03 19:26:43
FilePath: \LeetCode\198.打家劫舍.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
from readline import set_completion_display_matches_hook


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        first = nums[0]
        second = max(nums[0], nums[1])
        for i in range(2, n):
            first, second = second, max(first+nums[i], second)
        return second
# @lc code=end
