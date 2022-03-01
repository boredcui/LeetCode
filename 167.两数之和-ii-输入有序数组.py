'''
Author: Boredcui
Date: 2022-02-28 15:18:46
LastEditors: Boredcui
LastEditTime: 2022-02-28 15:47:01
FilePath: \LeetCode\167.两数之和-ii-输入有序数组.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n-1
        while left < right:
            if numbers[left]+numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left]+numbers[right] < target:
                left += 1
            else:
                right -= 1
        return[-1, -1]
# @lc code=end
