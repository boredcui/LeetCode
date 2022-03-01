'''
Author: Boredcui
Date: 2022-02-27 14:50:33
LastEditors: Boredcui
LastEditTime: 2022-02-27 16:31:57
FilePath: \LeetCode\5.最长回文子串.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        max_len = 1
        begin = 0
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        # 递推开始
        for Len in range(2, n+1):
            for i in range(n):
                j = Len+i-1
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j-i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and j-i+1 > max_len:
                    max_len = j-i+1
                    begin = i
        return s[begin:begin+max_len]
        # @lc code=end
