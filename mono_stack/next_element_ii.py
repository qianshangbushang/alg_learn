#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :next_element_ii.py
# @Time      :2022/7/6 10:35


from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        503. https://leetcode.cn/problems/next-greater-element-ii/
        :param nums:
        :return:
        """

        result = [-1] * len(nums)
        stack = []

        for idx in range(len(nums) * 2):
            idx = idx % len(nums)

            while len(stack) > 0 and nums[stack[-1]] < nums[idx]:
                result[stack[-1]] = nums[idx]
                stack.pop()
            stack.append(idx)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElements([1, 2, 1]))
    print(s.nextGreaterElements([1, 2, 3, 4, 3]))
