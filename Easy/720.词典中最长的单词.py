'''
Author: Boredcui
Date: 2022-03-17 14:09:11
LastEditors: Boredcui
LastEditTime: 2022-03-17 15:34:33
FilePath: \LeetCode\720.词典中最长的单词.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=720 lang=python3
#
# [720] 词典中最长的单词
#

# @lc code=start


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x: (-len(x), x), reverse=True)
        longest = ""
        candidates = {""}
        for word in words:
            if word[:-1] in candidates:
                longest = word
                candidates.add(word)
        return longest
        # @lc code=end
