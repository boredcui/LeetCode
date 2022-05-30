#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-05-30 14:05:09
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-05-30 14:28:05
FilePath: \LeetCode\1022.从根到叶的二进制数之和.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1022 lang=python3
#
# [1022] 从根到叶的二进制数之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(root, path):
            if root.left == None and root.right == None:
                res.append(path)
                return
            if root.left:
                dfs(root.left, path+str(root.left.val))
            if root.right:
                dfs(root.right, path+str(root.right.val))
        dfs(root, str(root.val))
        return sum([int(x, 2) for x in res])


# @lc code=end
