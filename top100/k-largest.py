#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :k-largest.py
# @Time      :2022/7/8 23:33


from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(start: int, end: int):
            if start == end:
                return start
            flag = nums[end]
            end = end
            while start < end:
                while start < end and nums[start] >= flag:
                    start += 1
                nums[end] = nums[start]

                while start < end and nums[end] < flag:
                    end -= 1
                nums[start] = nums[end]
                # print(start, end)
            nums[end] = flag
            return end

        def find(start, end):
            idx = partition(start, end)
            if idx == k - 1:
                return nums[idx]

            if idx < k - 1:
                return find(idx, end)

            return find(start, idx - 1)

        return find(0, len(nums) - 1)


if __name__ == '__main__':
    s = Solution()
    # print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
    print(s.findKthLargest([3, 2, 1, 5, 6, 4, 8, 9], 2))
