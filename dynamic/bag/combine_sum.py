#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :combine_sum.py
# @Time      :2022/7/2 21:02


from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        dp[i]  和为i的组合数

        dp[i] += dp[i - nums[j]]
        :param nums:
        :param target:
        :return:
        """
        if min(nums) > target:
            return 0
        dp = [0] * (target + 1)
        dp[0] = 1

        for x in range(1, target + 1):
            for y in nums:
                if y > x:
                    continue
                dp[x] = dp[x] + dp[x - y]
        return dp[target]


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum4([1, 2, 3], 4))
