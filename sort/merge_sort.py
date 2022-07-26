#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :merge_sort.py
# @Time      :2022/7/24 22:58


from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums

    def merge_sort(self, nums: List[int], low: int, high: int):
        if low >= high:
            return

        mid = low + (high - low) // 2
        self.merge_sort(nums, low, mid)
        self.merge_sort(nums, mid + 1, high)

        left, right, tmp = low, mid + 1, []
        while left <= mid and right <= high:
            if nums[left] < nums[right]:
                tmp.append(nums[left])
                left += 1
            else:
                tmp.append(nums[right])
                right += 1
        if left <= mid:
            tmp.extend(nums[left:mid + 1])
        elif right <= high:
            tmp.extend(nums[right:high + 1])
        nums[low:high + 1] = tmp
        return


if __name__ == '__main__':
    s = Solution()
    print(s.sortArray([5, 1, 1, 2, 0, 0]))
