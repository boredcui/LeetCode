'''
Author: Boredcui
Date: 2022-03-13 14:52:06
LastEditors: Boredcui
LastEditTime: 2022-03-13 15:21:46
FilePath: \LeetCode\393.utf-8-编码验证.py
Description:

Copyright (c) 2022 by boredcui, All Rights Reserved.
'''
#
# @lc app=leetcode.cn id=393 lang=python3
#
# [393] UTF-8 编码验证
#

# @lc code=start


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        MASK1, MASK2 = 1 << 7, (1 << 7) | (1 << 6)

        def getBytes(num: int) -> int:
            if (num & MASK1) == 0:
                return 1
            n, mask = 0, MASK1
            while num & mask:
                n += 1
                if n > 4:
                    return -1
                mask >>= 1
            return n if n >= 2 else -1

        index, m = 0, len(data)
        while index < m:
            n = getBytes(data[index])
            if n < 0 or index + n > m or any((ch & MASK2) != MASK1 for ch in data[index + 1: index + n]):
                return False
            index += n
        return True
        # @lc code=end
