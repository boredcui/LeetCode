'''
Author: Boredcui
Date: 2022-04-17 23:34:37
LastEditors: Boredcui
LastEditTime: 2022-04-17 23:35:02
FilePath: \LeetCode\819.最常见的单词.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#

# @lc code=start


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban = set(banned)
        freq = Counter()
        word, n = "", len(paragraph)
        for i in range(n + 1):
            if i < n and paragraph[i].isalpha():
                word += paragraph[i].lower()
            elif word:
                if word not in ban:
                    freq[word] += 1
                word = ""
        maxFreq = max(freq.values())
        return next(word for word, f in freq.items() if f == maxFreq)
# @lc code=end
