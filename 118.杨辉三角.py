'''
Author: Boredcui
Date: 2022-03-03 14:55:39
LastEditors: Boredcui
LastEditTime: 2022-03-03 15:24:32
FilePath: \LeetCode\118.杨辉三角.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = list()
        for i in range(numRows):
            row = list()
            for j in range(0, i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i-1][j-1]+ret[i-1][j])
            ret.append(row)
        return ret
# @lc code=end
