#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :revser_kstr.py
# @Time      :2022/7/7 11:43


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = [x for x in s]
        for i in range(0, len(s), 2 * k):
            self.reverse(arr, i, min(i + k, len(s)) - 1)
        return "".join(arr)

    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        return


if __name__ == '__main__':
    s = Solution()
    print(s.reverseStr("abcdefg", 2))
    print(s.reverseStr("abcd", 4))
