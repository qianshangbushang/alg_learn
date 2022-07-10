#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :valid_parent.py
# @Time      :2022/7/9 10:28


class Solution:
    def isValid(self, s: str) -> bool:
        col = []

        sign_dict = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch in sign_dict.values():
                col.append(ch)
                continue
            if len(col) == 0 or col.pop() != sign_dict[ch]:
                return False

        return len(col) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()[]{}"))
    print(s.isValid("([)]"))
