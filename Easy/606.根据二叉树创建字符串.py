'''
Author: Boredcui
Date: 2022-03-19 23:30:57
LastEditors: Boredcui
LastEditTime: 2022-03-19 23:31:21
FilePath: \LeetCode\606.根据二叉树创建字符串.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        if root.left is None and root.right is None:
            return str(root.val)
        if root.right is None:
            return f"{root.val}({self.tree2str(root.left)})"
        return f"{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})"
# @lc code=end
