'''
Author: Boredcui
Date: 2022-04-27 15:54:10
LastEditors: Boredcui
LastEditTime: 2022-04-27 15:54:30
FilePath: \LeetCode\417.太平洋大西洋水流问题.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=417 lang=python3
#
# [417] 太平洋大西洋水流问题
#

# @lc code=start


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def search(starts: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            visited = set()

            def dfs(x: int, y: int):
                if (x, y) in visited:
                    return
                visited.add((x, y))
                for nx, ny in ((x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)):
                    if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y]:
                        dfs(nx, ny)
            for x, y in starts:
                dfs(x, y)
            return visited

        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m - 1, i) for i in range(n)] + [(i, n - 1)
                                                     for i in range(m - 1)]
        return list(map(list, search(pacific) & search(atlantic)))
# @lc code=end
