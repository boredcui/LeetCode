'''
Author: Boredcui
Date: 2022-02-26 13:33:53
LastEditors: Boredcui
LastEditTime: 2022-03-07 14:50:52
FilePath: \LeetCode\Medium\2.两数相加.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
'''
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  - /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                       `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

           佛祖保佑     永不宕机     永无BUG
'''

'''
Author: Boredcui
Date: 2022-02-26 13:33:53
LastEditors: Boredcui
LastEditTime: 2022-02-26 15:22:51
FilePath: \LeetCode\2.两数相加.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode()
        carry = val = 0

        while carry or l1 or l2:
            val = carry
            if l1:
                l1, val = l1.next, l1.val+val
            if l2:
                l2, val = l2.next, l2.val+val
            carry, val = divmod(val, 10)
            curr.next = curr = ListNode(val)
        return head.next
# @lc code=end
