'''
Author: Boredcui
Date: 2022-04-04 19:31:12
LastEditors: Boredcui
LastEditTime: 2022-04-04 19:31:26
FilePath: \LeetCode\307.区域和检索-数组可修改.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=307 lang=python3
#
# [307] 区域和检索 - 数组可修改
#

# @lc code=start


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = [0] * (len(nums) + 1)
        for i, num in enumerate(nums, 1):
            self.add(i, num)

    def add(self, index: int, val: int):
        while index < len(self.tree):
            self.tree[index] += val
            index += index & -index

    def prefixSum(self, index) -> int:
        s = 0
        while index:
            s += self.tree[index]
            index &= index - 1
        return s

    def update(self, index: int, val: int) -> None:
        self.add(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum(right + 1) - self.prefixSum(left)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @lc code=end
