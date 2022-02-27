'''
Author: Boredcui
Date: 2022-02-26 20:32:27
LastEditors: Boredcui
LastEditTime: 2022-02-26 21:16:34
FilePath: \LeetCode\977.有序数组的平方.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        i, j, pos = 0, n-1, n-1
        while i <= j:
            if nums[i]*nums[i] > nums[j]*nums[j]:
                ans[pos] = nums[i]*nums[i]
                i += 1
            else:
                ans[pos] = nums[j]*nums[j]
                j -= 1
            pos -= 1
        return ans
        # @lc code=end
