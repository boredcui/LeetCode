'''
Author: Boredcui
Date: 2022-04-08 19:52:39
LastEditors: Boredcui
LastEditTime: 2022-04-08 19:53:47
FilePath: \LeetCode\429.n-叉树的层序遍历.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        ans = list()
        q = deque([root])

        while q:
            cnt = len(q)
            level = list()
            for _ in range(cnt):
                cur = q.popleft()
                level.append(cur.val)
                for child in cur.children:
                    q.append(child)
            ans.append(level)

        return ans
# @lc code=end
