#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :search.py
# @Time      :2022/7/14 10:44


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
                continue
            right = mid - 1

        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search([-1, 0, 3, 5, 9, 12], 9))
