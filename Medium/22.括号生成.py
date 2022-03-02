'''
Author: Boredcui
Date: 2022-03-01 21:49:50
LastEditors: Boredcui
LastEditTime: 2022-03-01 21:50:20
FilePath: \LeetCode\22.括号生成.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(s, left, right):
            if left == n == right:
                # 终止条件是括号数都是n
                res.append(s)
                return
            if right <= left <= n:
                # 如果左边的括号数大于右边的括号数且小于n则可以继续递归
                # 只要满足上述条件就一定还有分支有解
                dfs(s + '(', left+1, right)
                dfs(s + ')', left, right + 1)
        dfs('', 0, 0)
        return res
# @lc code=end
