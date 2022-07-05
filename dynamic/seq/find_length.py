#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :find_length.py
# @Time      :2022/7/5 10:39


from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        if nums1[i] == nums2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        :param nums1:
        :param nums2:
        :return:
        """

        dp = [[0 for _ in range(len(nums1) + 1)] for _ in range(len(nums2) + 1)]

        result = 0
        for i in range(len(nums2)):
            for j in range(len(nums1)):
                if nums2[i] == nums1[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                result = max(dp[i + 1][j + 1], result)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4]))
