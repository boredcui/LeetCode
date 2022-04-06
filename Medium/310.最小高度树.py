'''
Author: Boredcui
Date: 2022-04-06 15:07:55
LastEditors: Boredcui
LastEditTime: 2022-04-06 15:08:14
FilePath: \LeetCode\310.最小高度树.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=310 lang=python3
#
# [310] 最小高度树
#

# @lc code=start


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        g = [[] for _ in range(n)]
        deg = [0] * n
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            deg[x] += 1
            deg[y] += 1

        q = [i for i, d in enumerate(deg) if d == 1]
        remainNodes = n
        while remainNodes > 2:
            remainNodes -= len(q)
            tmp = q
            q = []
            for x in tmp:
                for y in g[x]:
                    deg[y] -= 1
                    if deg[y] == 1:
                        q.append(y)
        return q
# @lc code=end
