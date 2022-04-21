'''
Author: Boredcui
Date: 2022-04-21 20:17:05
LastEditors: Boredcui
LastEditTime: 2022-04-21 20:17:17
FilePath: \LeetCode\824.山羊拉丁文.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=824 lang=python3
#
# [824] 山羊拉丁文
#

# @lc code=start
VOWEL_SET = set('aeiouAEIOU')


class Solution:
    def toGoatLatin(self, S: str) -> str:
        return ' '.join((word if word[0] in VOWEL_SET else word[1:] + word[0]) + 'ma' + (idx+1)*'a'
                        for idx, word in enumerate(S.split()))
# @lc code=end
