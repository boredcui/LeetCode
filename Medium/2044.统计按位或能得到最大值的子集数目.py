#
# @lc app=leetcode.cn id=2044 lang=python3
#
# [2044] 统计按位或能得到最大值的子集数目
#

# @lc code=start
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr, cnt = 0, 0
        for i in range(1, 1 << len(nums)):
            orVal = reduce(
                or_, (num for j, num in enumerate(nums) if (i >> j) & 1), 0)
            if orVal > maxOr:
                maxOr, cnt = orVal, 1
            elif orVal == maxOr:
                cnt += 1
        return cnt
# @lc code=end
