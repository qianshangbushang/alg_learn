#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :lis.py
# @Time      :2022/7/13 10:46


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        dp[i] 表示以i结尾的最长子序列长度
        :param nums:
        :return:
        """

        dp = [1] * len(nums)

        result = dp[0]
        for idx in range(1, len(nums)):
            for idy in range(0, idx):
                if nums[idy] < nums[idx]:
                    dp[idx] = max(dp[idx], dp[idy] + 1)
            result = max(dp[idx], result)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
