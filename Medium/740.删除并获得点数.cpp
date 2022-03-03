/*
 * @Author: Boredcui
 * @Date: 2022-03-03 20:38:17
 * @LastEditors: Boredcui
 * @LastEditTime: 2022-03-03 20:46:50
 * @FilePath: \LeetCode\740.删除并获得点数.cpp
 * @Description:
 *
 * Copyright (c) 2022 by boredcui, All Rights Reserved.
 */
/*
 * @lc app=leetcode.cn id=740 lang=cpp
 *
 * [740] 删除并获得点数
 */

// @lc code=start
class Solution
{
private:
    int rob(vector<int> &nums)
    {
        int size = nums.size();
        int first = nums[0], second = max(nums[0], nums[1]);
        for (int i = 2; i < size; ++i)
        {
            int temp = second;
            second = max(first + nums[i], second);
            first = temp;
        }
        return second;
    }

public:
    int deleteAndEarn(vector<int> &nums)
    {
        int maxVal = 0;
        for (int val : nums)
        {
            maxVal = max(val, maxVal);
        }
        vector<int> sum(maxVal + 1);
        for (int val : nums)
        {
            sum[val] += val;
        }
        return rob(sum);
    }
};
// @lc code=end
