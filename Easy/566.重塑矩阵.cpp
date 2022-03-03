/*
 * @Author: Boredcui
 * @Date: 2022-03-03 14:46:59
 * @LastEditors: Boredcui
 * @LastEditTime: 2022-03-03 14:54:22
 * @FilePath: \LeetCode\566.重塑矩阵.cpp
 * @Description:
 *
 * Copyright (c) 2022 by boredcui, All Rights Reserved.
 */
/*
 * @lc app=leetcode.cn id=566 lang=cpp
 *
 * [566] 重塑矩阵
 */

// @lc code=start
class Solution
{
public:
    vector<vector<int>> matrixReshape(vector<vector<int>> &mat, int r, int c)
    {
        int m = mat.size();
        int n = mat[0].size();

        if (m * n != r * c)
        {
            return mat;
        }

        vector<vector<int>> ans(r, vector<int>(c));
        for (int x = 0; x < m * n; ++x)
        {
            ans[x / c][x % c] = mat[x / n][x % n];
        }
        return ans;
    }
};
// @lc code=end
