/*
 * @Author: Boredcui
 * @Date: 2022-03-03 14:05:54
 * @LastEditors: Boredcui
 * @LastEditTime: 2022-03-03 14:10:48
 * @FilePath: \LeetCode\258.各位相加.cpp
 * @Description:
 *
 * Copyright (c) 2022 by boredcui, All Rights Reserved.
 */
/*
 * @lc app=leetcode.cn id=258 lang=cpp
 *
 * [258] 各位相加
 */

// @lc code=start
class Solution
{
public:
    int addDigits(int num)
    {
        while (num >= 10)
        {
            num = num % 10 + (num / 10);
        }
        return num;
    }
};
// @lc code=end
