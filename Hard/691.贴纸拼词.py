#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-05-14 14:11:30
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-05-14 14:11:32
FilePath: \LeetCode\Hard\691.贴纸拼词.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-05-14 14:06:34
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-05-14 14:11:05
FilePath: \LeetCode\691.贴纸拼词.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=691 lang=python3
#
# [691] 贴纸拼词
#

# @lc code=start


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        m = len(target)

        @cache
        def dp(mask: int) -> int:
            if mask == 0:
                return 0
            res = m + 1
            for sticker in stickers:
                left = mask
                cnt = Counter(sticker)
                for i, c in enumerate(target):
                    if mask >> i & 1 and cnt[c]:
                        cnt[c] -= 1
                        left ^= 1 << i
                if left < mask:
                    res = min(res, dp(left) + 1)
            return res
        res = dp((1 << m) - 1)
        return res if res <= m else -1
# @lc code=end
