'''
Author: Boredcui
Date: 2022-03-24 14:32:54
LastEditors: Boredcui
LastEditTime: 2022-03-24 14:33:11
FilePath: \LeetCode\661.图片平滑器.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#

# @lc code=start


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                tot, num = 0, 0
                for x in range(max(i - 1, 0), min(i + 2, m)):
                    for y in range(max(j - 1, 0), min(j + 2, n)):
                        tot += img[x][y]
                        num += 1
                ans[i][j] = tot // num
        return ans
# @lc code=end
