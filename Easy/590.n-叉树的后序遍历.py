'''
Author: Boredcui
Date: 2022-03-12 17:51:40
LastEditors: Boredcui
LastEditTime: 2022-03-12 18:03:35
FilePath: \LeetCode\590.n-叉树的后序遍历.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N 叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []

        def dfs(node: 'Node'):
            if node is None:
                return
            for ch in node.children:
                dfs(ch)
            ans.append(node.val)
        dfs(root)
        return ans
# @lc code=end
