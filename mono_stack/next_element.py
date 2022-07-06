#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :next_element.py
# @Time      :2022/7/6 10:25


from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        496. https://leetcode.cn/problems/next-greater-element-i/
        :param nums1:
        :param nums2:
        :return:
        """

        result = [-1] * len(nums1)
        stack = []

        for idx in range(len(nums2)):
            while len(stack) > 0 and nums2[stack[-1]] < nums2[idx]:
                if nums2[stack[-1]] in nums1:
                    ridx = nums1.index(nums2[stack[-1]])
                    result[ridx] = nums2[idx]
                stack.pop()
            stack.append(idx)

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
