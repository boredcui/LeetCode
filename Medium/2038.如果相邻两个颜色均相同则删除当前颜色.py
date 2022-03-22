'''
Author: Boredcui
Date: 2022-03-22 15:34:42
LastEditors: Boredcui
LastEditTime: 2022-03-22 17:10:54
FilePath: \LeetCode\2038.如果相邻两个颜色均相同则删除当前颜色.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2038 lang=python3
#
# [2038] 如果相邻两个颜色均相同则删除当前颜色
#

# @lc code=start


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        freq = [0, 0]
        cur, cnt = 'C', 0
        # 不同字母计数转换技巧
        for C in colors:
            if C != cur:
                cnt = 1
                cur = C
            else:
                cnt += 1
                # 只要大于3就计数一次，直到下一个字符与当前字母不同
                if cnt >= 3:
                    freq[ord(cur)-ord('A')] += 1
        return freq[0] > freq[1]
        # @lc code=end
