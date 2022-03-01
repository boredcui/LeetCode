'''
Author: Boredcui
Date: 2022-02-26 16:55:16
LastEditors: Boredcui
LastEditTime: 2022-02-26 18:13:42
FilePath: \LeetCode\35.搜索插入位置.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (high+low)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid+1
            else:
                high = mid-1
        return low
        # @lc code=end
