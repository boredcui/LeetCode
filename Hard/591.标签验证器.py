'''
Author: Boredcui
Date: 2022-05-02 16:41:16
LastEditors: Boredcui
LastEditTime: 2022-05-02 18:18:28
FilePath: \LeetCode\591.标签验证器.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=591 lang=python3
#
# [591] 标签验证器
#

# @lc code=start


class Solution:
    def isValid(self, code: str) -> bool:
        code = re.sub(r'<!\[CDATA\[.*?\]\]>|t', '-', code)
        prev = None
        while code != prev:
            prev = code
            code = re.sub(r'<([A-Z]{1,9})>[^<]*</\1>', 't', code)
        return code == 't'
# @lc code=end
