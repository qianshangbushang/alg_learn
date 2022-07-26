#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :quick_sort.py
# @Time      :2022/7/24 23:45
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.partition(nums, 0, len(nums) - 1)
        return nums

    def partition(self, nums: List[int], low: int, high: int):
        if low >= high:
            return

        mid = low + (high - low) // 2
        nums[high], nums[mid] = nums[mid], nums[high]
        pivot = nums[high]
        left, right = low, high

        while left < right:
            while left < right and nums[left] < pivot:
                left += 1
            nums[right] = nums[left]  # pivot 在最后，一定不满足nums[left] < pivot

            # nums[left] > pivot 成立
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]  # 当left == right,  顶多是执行nums[left] = nums[left]
        nums[left] = pivot

        self.partition(nums, low, left - 1)
        self.partition(nums, left + 1, high)
        return


if __name__ == '__main__':
    s = Solution()
    print(s.sortArray([5, 1, 1, 2, 0, 0]))
