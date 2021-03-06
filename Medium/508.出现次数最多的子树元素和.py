#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-06-19 21:22:02
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-06-19 21:23:00
FilePath: \LeetCode\508.出现次数最多的子树元素和.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=508 lang=python3
#
# [508] 出现次数最多的子树元素和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        cnt = Counter()

        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0
            sum = node.val + dfs(node.left) + dfs(node.right)
            cnt[sum] += 1
            return sum
        dfs(root)

        maxCnt = max(cnt.values())
        return [s for s, c in cnt.items() if c == maxCnt]

# @lc code=end
