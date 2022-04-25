'''
Author: Boredcui
Date: 2022-04-25 13:46:01
LastEditors: Boredcui
LastEditTime: 2022-04-25 15:44:07
FilePath: \LeetCode\868.二进制间距.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=868 lang=python3
#
# [868] 二进制间距
#

# @lc code=start


class Solution:
    def binaryGap(self, n: int) -> int:
        last, ans, i = -1, 0, 0
        while n:
            if n & 1:
                if last != -1:
                    ans = max(ans, i - last)
                last = i
            n >>= 1
            i += 1
        return ans
# @lc code=end
