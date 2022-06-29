#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-06-29 21:49:45
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-06-29 21:50:10
FilePath: \LeetCode\535.tiny-url-的加密与解密.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=535 lang=python3
#
# [535] TinyURL 的加密与解密
#

# @lc code=start
class Codec:
    def __init__(self):
        self.database = {}
        self.id = 0

    def encode(self, longUrl: str) -> str:
        self.id += 1
        self.database[self.id] = longUrl
        return "http://tinyurl.com/" + str(self.id)

    def decode(self, shortUrl: str) -> str:
        i = shortUrl.rfind('/')
        id = int(shortUrl[i + 1:])
        return self.database[id]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end
