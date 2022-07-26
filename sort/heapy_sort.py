#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :heapy_sort.py
# @Time      :2022/7/25 0:26


from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n // 2 - 1, -1, -1):
            self.heapy_sort(nums, i, n - 1)

        for j in range(n - 1, -1, -1):
            nums[0], nums[j] = nums[j], nums[0]
            self.heapy_sort(nums, 0, j - 1)
        return nums

    def heapy_sort(self, nums: List[int], i: int, end: int):
        j = 2 * i + 1

        while j <= end:
            if j + 1 <= end and nums[j] < nums[j + 1]:
                j += 1
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i = j
                j = 2 * i + 1
            else:
                break
        return


if __name__ == '__main__':
    s = Solution()
    print(s.sortArray([9, 6, 8, 2, 5, 1]))
