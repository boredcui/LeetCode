'''
Author: Boredcui
Date: 2022-02-26 13:04:27
LastEditors: Boredcui
LastEditTime: 2022-02-26 13:31:01
FilePath: \LeetCode\2016.增量元素之间的最大差值.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2016 lang=python3
#
# [2016] 增量元素之间的最大差值
#

# @lc code=start


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans, min = -1, nums[0]
        for i in range(1, n):
            if nums[i] > min:
                ans = max(ans, nums[i]-min)
            else:
                min = nums[i]
        return ans

# @lc code=end
