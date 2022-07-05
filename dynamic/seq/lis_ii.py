#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :lis_ii.py
# @Time      :2022/7/5 10:19


from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        if nums[i] > nums[i-1]:
            dp[i] = dp[i-1] + 1
        :param nums:
        :return:
        """

        dp = [1] * len(nums)
        result = 1
        for idx in range(1, len(nums)):
            if nums[idx] > nums[idx - 1]:
                dp[idx] = dp[idx - 1] + 1
            result = max(result, dp[idx])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.findLengthOfLCIS([1, 3, 5, 4, 7]))
