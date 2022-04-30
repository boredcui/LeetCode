'''
Author: Boredcui
Date: 2022-04-30 16:10:19
LastEditors: Boredcui
LastEditTime: 2022-04-30 16:18:49
FilePath: \LeetCode\908.最小差值-i.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=908 lang=python3
#
# [908] 最小差值 I
#

# @lc code=start


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0, max(nums) - min(nums) - 2 * k)
# @lc code=end
