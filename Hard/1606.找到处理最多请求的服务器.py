'''
Author: Boredcui
Date: 2022-03-30 18:52:24
LastEditors: Boredcui
LastEditTime: 2022-03-30 19:57:46
FilePath: \LeetCode\1606.找到处理最多请求的服务器.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1606 lang=python3
#
# [1606] 找到处理最多请求的服务器
#

# @lc code=start


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = list(range(k))
        busy = []
        requests = [0] * k
        for i, (start, t) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                _, id = heappop(busy)
                heappush(available, i + (id - i) %
                         k)  # 利用 Python 负数取模变成同余的非负数的性质
            if available:
                id = heappop(available) % k
                requests[id] += 1
                heappush(busy, (start + t, id))
        maxRequest = max(requests)
        return [i for i, req in enumerate(requests) if req == maxRequest]
        # @lc code=end
