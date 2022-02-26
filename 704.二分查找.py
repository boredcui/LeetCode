'''
Author: Boredcui
Date: 2022-02-26 15:49:27
LastEditors: Boredcui
LastEditTime: 2022-02-26 16:09:28
FilePath: \LeetCode\704.二分查找.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (high-low)//2+low
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid+1
            elif target < nums[mid]:
                high = mid-1
        return -1
# @lc code=end
