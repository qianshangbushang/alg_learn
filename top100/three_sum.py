#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :three_sum.py
# @Time      :2022/7/9 2:49


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort(key=lambda x: x)
        result = []
        for idx in range(len(nums) - 2):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            left = idx + 1
            right = len(nums) - 1
            print(f"processing {idx}")
            while left < right:
                if nums[idx] + nums[left] + nums[right] < 0:
                    left += 1
                    continue
                if nums[idx] + nums[left] + nums[right] > 0:
                    right -= 1
                    continue
                result.append([nums[idx], nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

                right -= 1
                while nums[right] == nums[right + 1] and left < right:
                    right -= 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([0, 0, 0, 0], ))
