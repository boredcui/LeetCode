'''
Author: Boredcui
Date: 2022-03-01 18:37:49
LastEditors: Boredcui
LastEditTime: 2022-03-01 19:16:30
FilePath: \LeetCode\19.删除链表的倒数第-n-个结点.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dumy = ListNode(0, head)
        first = head
        second = dumy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dumy.next
# @lc code=end
