#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-06-22 22:55:34
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-06-22 22:56:00
FilePath: \LeetCode\513.找树左下角的值.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        curVal = curHeight = 0

        def dfs(node: Optional[TreeNode], height: int) -> None:
            if node is None:
                return
            height += 1
            dfs(node.left, height)
            dfs(node.right, height)
            nonlocal curVal, curHeight
            if height > curHeight:
                curHeight = height
                curVal = node.val
        dfs(root, 0)
        return curVal

# @lc code=end
