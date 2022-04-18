'''
Author: Boredcui
Date: 2022-04-18 20:00:32
LastEditors: Boredcui
LastEditTime: 2022-04-18 20:02:04
FilePath: \LeetCode\386.字典序排数.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=386 lang=python3
#
# [386] 字典序排数
#

# @lc code=start


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [0] * n
        num = 1
        for i in range(n):
            ans[i] = num
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num + 1 > n:
                    num //= 10
                num += 1
        return ans
# @lc code=end
