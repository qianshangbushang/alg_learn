#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :merge_arr.py
# @Time      :2022/7/9 13:58


from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums2[n - 1] > nums1[m - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n = n - 1
                continue
            nums1[m + n - 1] = nums1[m - 1]
            m = m - 1

        while m > 0:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        while n > 0:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
        return


if __name__ == '__main__':
    s = Solution()
    num1 = [1, 2, 3, 0, 0, 0]
    print(s.merge(num1, 3, [2, 5, 6], 3))
    print(num1)
