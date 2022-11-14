#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :non_increasing_arr.py
# @Time      :2022/11/11 10:09


from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        flag = True
        for i in range(1, len(nums)):
            # 3 4 2
            cond1 = i - 2 >= 0 and nums[i] < nums[i - 2]
            if cond1 and flag:
                nums[i] = nums[i - 1]
                flag = False
                continue

            # 3 5 4
            cond2 = i - 1 >= 0 and nums[i] < nums[i - 1]
            if cond2 and flag:
                nums[i - 1] = nums[i]
                flag = False
                continue

            if nums[i] < nums[i - 1]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.checkPossibility([4, 2, 1]))
