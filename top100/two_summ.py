#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :two_summ.py
# @Time      :2022/7/9 10:12


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for idx in range(len(nums)):
            if (target - nums[idx]) in num_map:
                return [num_map[target - nums[idx]], idx]
            num_map[nums[idx]] = idx
        return []

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        low, high = 0, len(nums) - 1

        while low < high:
            if nums[low] + nums[high] == target:
                return [nums[low], nums[high]]
            if nums[low] + nums[high] < target:
                low += 1

            if nums[low] + nums[high] > target:
                high -= 1
        return []


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
