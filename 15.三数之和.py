'''
Author: Boredcui
Date: 2022-02-27 17:53:35
LastEditors: Boredcui
LastEditTime: 2022-02-27 20:17:04
FilePath: \LeetCode\15.三数之和.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[i]+nums[j]+nums[k] > 0:
                    k = k-1
                    while k > 0 and nums[k] == nums[k+1]:
                        k = k-1
                elif nums[i]+nums[j]+nums[k] < 0:
                    j = j+1
                    while j < len(nums) and nums[j] == nums[j-1]:
                        j = j+1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    k = k-1
                    while k > 0 and nums[k] == nums[k+1]:
                        k = k-1
                    j = j+1
                    while j < len(nums) and nums[j] == nums[j-1]:
                        j = j+1
        return result
# @lc code=end
