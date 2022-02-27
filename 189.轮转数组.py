'''
Author: Boredcui
Date: 2022-02-26 21:21:47
LastEditors: Boredcui
LastEditTime: 2022-02-27 12:48:05
FilePath: \LeetCode\189.轮转数组.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#

# @lc code=start


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ans = [0]*n
        ans[0:k % n] = nums[n-(k % n):n]
        ans[k % n:n] = nums[0:n-(k % n)]
        for i in range(0, n):
            nums[i] = ans[i]

# @lc code=end
