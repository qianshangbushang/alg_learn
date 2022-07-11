#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :permute.py
# @Time      :2022/7/11 14:41


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def trace(exist_dict: dict, path: List[int]):
            if len(exist_dict) == len(nums):
                result.append(path.copy())
                return

            for x in nums:
                if x in exist_dict:
                    continue
                path.append(x)
                exist_dict[x] = 1
                trace(exist_dict, path)
                del exist_dict[x]
                path.pop()

        trace({}, [])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
