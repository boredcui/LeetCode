'''
Author: Boredcui
Date: 2022-02-27 12:51:39
LastEditors: Boredcui
LastEditTime: 2022-02-27 13:11:12
FilePath: \LeetCode\553.最优除法.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=553 lang=python3
#
# [553] 最优除法
#

# @lc code=start


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0])+'/'+str(nums[1])
        return str(nums[0])+'/('+'/'.join(map(str, nums[1:]))+')'
# @lc code=end
