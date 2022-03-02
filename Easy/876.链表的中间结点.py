'''
Author: Boredcui
Date: 2022-03-02 12:14:54
LastEditors: Boredcui
LastEditTime: 2022-03-02 12:24:26
FilePath: \LeetCode\876.链表的中间结点.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from distutils.command.build_scripts import first_line_re


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
# @lc code=end
