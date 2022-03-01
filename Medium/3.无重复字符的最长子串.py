#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ooc = set()
        n = len(s)
        ans, rk = 0, -1
        for i in range(0, n):
            if i != 0:
                ooc.remove(s[i-1])
            while rk+1 < n and s[rk+1] not in ooc:
                ooc.add(s[rk+1])
                rk += 1
            ans = max(ans, rk-i+1)
        return ans

# @lc code=end
