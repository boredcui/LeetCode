'''
Author: Boredcui
Date: 2022-03-03 20:07:15
LastEditors: Boredcui
LastEditTime: 2022-03-03 20:35:59
FilePath: \LeetCode\740.删除并获得点数.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=740 lang=python3
#
# [740] 删除并获得点数
#

# @lc code=start


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        total = [0]*(max(nums)+1)
        for val in nums:
            total[val] += val

        def rob(nums: List[int]) -> int:
            n = len(nums)
            first, second = nums[0], max(nums[0], nums[1])
            for i in range(2, n):
                first, second = second, max(first+nums[i], second)
            return second

        return rob(total)
# @lc code=end
