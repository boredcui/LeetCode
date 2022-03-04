'''
Author: Boredcui
Date: 2022-03-04 13:19:56
LastEditors: Boredcui
LastEditTime: 2022-03-04 13:54:31
FilePath: \LeetCode\733.图像渲染.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

# @lc code=start


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        currColor = image[sr][sc]

        def dfs(x: int, y: int):
            if image[x][y] == currColor:
                image[x][y] = newColor
                for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= mx < n and 0 <= my < m and image[mx][my] == currColor:
                        dfs(mx, my)

        if currColor != newColor:
            dfs(sr, sc)
        return image

# @lc code=end
