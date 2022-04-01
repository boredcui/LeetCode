'''
Author: Boredcui
Date: 2022-04-01 19:20:52
LastEditors: Boredcui
LastEditTime: 2022-04-01 19:58:13
FilePath: \LeetCode\954.二倍数对数组.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=954 lang=python3
#
# [954] 二倍数对数组
#

# @lc code=start


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        if cnt[0] % 2:
            return False
        for x in sorted(cnt, key=abs):
            if cnt[2 * x] < cnt[x]:  # 无法找到足够的 2x 与 x 配对
                return False
            cnt[2 * x] -= cnt[x]
        return True
        # @lc code=end
