'''
Author: Boredcui
Date: 2022-05-01 17:42:32
LastEditors: Boredcui
LastEditTime: 2022-05-01 17:54:57
FilePath: \LeetCode\1305.两棵二叉搜索树中的所有元素.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1305 lang=python3
#
# [1305] 两棵二叉搜索树中的所有元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node: TreeNode, res: List[int]):
            if node:
                inorder(node.left, res)
                res.append(node.val)
                inorder(node.right, res)

        nums1, nums2 = [], []
        inorder(root1, nums1)
        inorder(root2, nums2)

        merged = []
        p1, n1 = 0, len(nums1)
        p2, n2 = 0, len(nums2)
        while True:
            if p1 == n1:
                merged.extend(nums2[p2:])
                break
            if p2 == n2:
                merged.extend(nums1[p1:])
                break
            if nums1[p1] < nums2[p2]:
                merged.append(nums1[p1])
                p1 += 1
            else:
                merged.append(nums2[p2])
                p2 += 1
        return merged

# @lc code=end
