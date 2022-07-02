#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-07-02 23:19:30
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-07-02 23:19:32
FilePath: \LeetCode\DP\871.最低加油次数.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-07-02 23:18:57
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-07-02 23:19:22
FilePath: \LeetCode\871.最低加油次数.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=871 lang=python3
#
# [871] 最低加油次数
#

# @lc code=start


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel] + [0] * len(stations)
        for i, (pos, fuel) in enumerate(stations):
            for j in range(i, -1, -1):
                if dp[j] >= pos:
                    dp[j + 1] = max(dp[j + 1], dp[j] + fuel)
        return next((i for i, v in enumerate(dp) if v >= target), -1)

# @lc code=end
