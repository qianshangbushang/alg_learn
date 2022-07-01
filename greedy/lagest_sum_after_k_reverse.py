#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :lagest_sum_after_k_reverse.py
# @Time      :2022/7/1 10:14


from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, key=lambda x: abs(x), reverse=True)
        for idx in range(len(nums)):
            if k <= 0:
                break
            if nums[idx] < 0:
                k -= 1
                nums[idx] *= -1

        while k > 0:
            nums[-1] *= -1
            k -= 1

        return sum(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.largestSumAfterKNegations([4, 5, 3], k=1))
