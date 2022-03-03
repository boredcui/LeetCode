/*
 * @Author: Boredcui
 * @Date: 2022-03-03 15:25:18
 * @LastEditors: Boredcui
 * @LastEditTime: 2022-03-03 15:30:09
 * @FilePath: \LeetCode\118.杨辉三角.cpp
 * @Description:
 *
 * Copyright (c) 2022 by boredcui, All Rights Reserved.
 */
/*
 * @lc app=leetcode.cn id=118 lang=cpp
 *
 * [118] 杨辉三角
 */

// @lc code=start
class Solution
{
public:
    vector<vector<int>> generate(int numRows)
    {
        vector<vector<int>> ret(numRows);
        for (int i = 0; i < numRows; ++i)
        {
            ret[i].resize(i + 1);
            ret[i][0] = ret[i][i] = 1;
            for (int j = 1; j < i; ++j)
            {
                ret[i][j] = ret[i - 1][j - 1] + ret[i - 1][j];
            }
        }
        return ret;
    }
};
// @lc code=end
