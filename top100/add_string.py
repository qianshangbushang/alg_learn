#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :add_string.py
# @Time      :2022/7/12 10:58


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len_1 = len(num1)
        len_2 = len(num2)

        result = []
        last_left = 0
        while len_1 > 0 or len_2 > 0:
            ch_1 = num1[len_1 - 1] if len_1 >= 1 else '0'
            ch_2 = num2[len_2 - 1] if len_2 >= 1 else '0'
            cur = ord(ch_1) + ord(ch_2) - 2 * ord('0') + last_left
            result.append(chr(cur % 10 + ord('0')))
            last_left = cur // 10
            len_1 -= 1
            len_2 -= 1
        if last_left:
            result.append(chr(last_left + ord('0')))
        return "".join(result[::-1])


if __name__ == '__main__':
    s = Solution()
    print(s.addStrings("123", "11"))
    print(s.addStrings("1", "9"))
