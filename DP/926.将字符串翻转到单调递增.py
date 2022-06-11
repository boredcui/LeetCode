#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-06-11 20:54:36
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-06-11 20:54:38
FilePath: \LeetCode\DP\926.将字符串翻转到单调递增.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-06-11 20:52:34
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-06-11 20:54:22
FilePath: \LeetCode\926.将字符串翻转到单调递增.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=926 lang=python3
#
# [926] 将字符串翻转到单调递增
#

# @lc code=start


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp0 = dp1 = 0
        for c in s:
            dp0New, dp1New = dp0, min(dp0, dp1)
            if c == '1':
                dp0New += 1
            else:
                dp1New += 1
            dp0, dp1 = dp0New, dp1New
        return min(dp0, dp1)

# @lc code=end
