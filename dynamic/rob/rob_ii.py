#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :rob_ii.py
# @Time      :2022/7/3 23:59


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dp[i] 包括房间i在内的最大收益
        dp[i] = max(dp[i-2]  + nums[i], dp[i - 1])
        :param nums:
        :return:
        """
        f1 = self.rob_range(nums, 0, len(nums) - 1)
        f2 = self.rob_range(nums, 1, len(nums))
        return max(f1, f2)

    def rob_range(self, nums, start, end):
        if end - start <= 1:
            return 0
        if end - start <= 2:
            return max(nums[start: end])

        a = nums[start]
        b = max(nums[start:start + 2])

        for idx in range(start + 2, end):
            a, b = b, max(a + nums[idx], b)
        return b


if __name__ == '__main__':
    s = Solution()
    print(s.rob([1, 6, 1, 9, 1]))
