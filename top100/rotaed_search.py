#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :rotaed_search.py
# @Time      :2022/7/9 13:00


from typing import List


class Solution:

    def search1(self, nums: List[int], target: int) -> int:
        def find(start, end):
            if start > end:
                return -1
            mid = (end - start) // 2 + start
            if nums[mid] < target:
                return find(mid + 1, end)
            if nums[mid] > target:
                return find(start, mid - 1)
            return mid

        # idx = 0
        # while nums[idx + 1] > nums[idx]:
        #     idx += 1
        idx = 0
        while idx + 1 < len(nums) and nums[idx + 1] > nums[idx]:
            idx += 1

        if target > nums[0]:
            return find(0, idx)
        elif target < nums[0]:
            return find(idx + 1, len(nums) - 1)
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    # print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
    # print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
    print(s.search([1, 3], 1))
