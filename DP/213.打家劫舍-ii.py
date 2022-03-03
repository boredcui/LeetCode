'''
Author: Boredcui
Date: 2022-03-03 19:28:16
LastEditors: Boredcui
LastEditTime: 2022-03-03 20:06:18
FilePath: \LeetCode\213.打家劫舍-ii.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start


from operator import length_hint


class Solution:
    def rob(self, nums: List[int]) -> int:
        def robRange(start: int, end: int) -> int:
            first = nums[start]
            second = max(nums[start], nums[start+1])
            for i in range(start+2, end):
                first, second = second, max(first+nums[i], second)
            return second

        length = len(nums)
        if length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])
        else:
            return max(robRange(0, length-1), robRange(1, length))
# @lc code=end
