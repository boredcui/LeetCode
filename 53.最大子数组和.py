'''
Author: Boredcui
Date: 2022-02-28 20:36:36
LastEditors: Boredcui
LastEditTime: 2022-02-28 21:09:28
FilePath: \LeetCode\53.最大子数组和.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]

        return max(nums)
# @lc code=end
