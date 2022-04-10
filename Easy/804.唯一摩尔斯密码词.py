'''
Author: Boredcui
Date: 2022-04-10 19:15:12
LastEditors: Boredcui
LastEditTime: 2022-04-10 19:15:30
FilePath: \LeetCode\804.唯一摩尔斯密码词.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=804 lang=python3
#
# [804] 唯一摩尔斯密码词
#

# @lc code=start
MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
         "....", "..", ".---", "-.-", ".-..", "--", "-.",
         "---", ".--.", "--.-", ".-.", "...", "-", "..-",
         "...-", ".--", "-..-", "-.--", "--.."]


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len(set("".join(MORSE[ord(ch) - ord('a')] for ch in word) for word in words))
# @lc code=end
