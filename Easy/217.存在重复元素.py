'''
Author: Boredcui
Date: 2022-02-28 20:32:05
LastEditors: Boredcui
LastEditTime: 2022-02-28 20:34:01
FilePath: \LeetCode\217.存在重复元素.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashtable = dict()
        for i, num in enumerate(nums):
            hashtable[nums[i]] = i
        if len(nums) == len(hashtable):
            return False
        return True
# @lc code=end
