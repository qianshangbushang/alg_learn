#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :fl_pos.py
# @Time      :2022/10/27 14:10


from collections import defaultdict
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        def lsearch(nums: List[int], target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    if mid != 0 and nums[mid - 1] == target:
                        right = mid - 1
                    else:
                        return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        def rsearch(nums: List[int], target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    if mid != len(nums) - 1 and nums[mid + 1] == target:
                        left = mid + 1
                    else:
                        return mid

                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        lidx = lsearch(nums, target)
        ridx = rsearch(nums, target)

        return [lidx, ridx]


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5,7,7,8,8,10], 8))