#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :find_idx.py
# @Time      :2022/10/31 13:54


from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        lidx = self.find_left_idx(nums, target)
        ridx = self.find_right_idx(nums, target)
        if lidx == ridx == -1:
            return []
        return list(range(lidx, ridx + 1))

    def find_left_idx(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right + 1 - left) // 2
            if nums[mid] == target:
                right = mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        print(left, nums[left], right, nums[right])
        if nums[left] == target:
            return left
        return -1

    def find_right_idx(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if nums[left] == target:
            return left
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.targetIndices([1, 2, 5, 2, 3], 2))
    print(s.targetIndices([1, 2, 5, 2, 3], 3))
    print(s.targetIndices([1, 2, 5, 2, 3], 4))
    print(s.targetIndices([1, 2, 5, 2, 3], 5))
    print(s.targetIndices([100, 1, 100], 100))
