'''
Author: Boredcui
Date: 2022-02-25 10:48:07
LastEditors: Boredcui
LastEditTime: 2022-02-25 16:45:52
FilePath: \LeetCode\1.两数之和.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''

# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
# enumeration
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         for i in range(n):
#             for j in range(i+1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# Hashtable


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target-num], i]
            hashtable[nums[i]] = i
        return[]
# @lc code=end
