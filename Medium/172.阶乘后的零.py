'''
Author: Boredcui
Date: 2022-03-25 18:27:56
LastEditors: Boredcui
LastEditTime: 2022-03-25 18:28:08
FilePath: \LeetCode\172.阶乘后的零.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start


class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n:
            n //= 5
            ans += n
        return ans

# @lc code=end
