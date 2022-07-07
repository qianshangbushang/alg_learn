#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :remove_element.py
# @Time      :2022/7/7 10:21


from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        27. https://leetcode-cn.com/problems/remove-element/
        :param nums:
        :param val:
        :return:
        """
        point = -1
        for idx in range(len(nums)):
            if nums[idx] == val:
                continue
            point += 1
            nums[point] = nums[idx]
        return nums[:point + 1]


if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([3, 2, 2, 3], 3))
