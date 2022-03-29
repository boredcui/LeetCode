'''
Author: Boredcui
Date: 2022-03-29 21:45:48
LastEditors: Boredcui
LastEditTime: 2022-03-29 21:55:21
FilePath: \LeetCode\2024.考试的最大困扰度.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2024 lang=python3
#
# [2024] 考试的最大困扰度
#

# @lc code=start


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxConsecutiveChar(ch: str) -> int:
            ans, left, sum = 0, 0, 0
            for right in range(len(answerKey)):
                sum += answerKey[right] != ch
                while sum > k:
                    sum -= answerKey[left] != ch
                    left += 1
                ans = max(ans, right - left + 1)
            return ans
        return max(maxConsecutiveChar('T'), maxConsecutiveChar('F'))
        # @lc code=end
