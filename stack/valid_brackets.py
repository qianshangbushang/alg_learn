# -*- coding: utf-8 -*-
# @Time    : 2020/10/9 22:08
class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        backet_map = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        for x in s:
            if x in ['(', '{', "["]:
                arr.append(x)
                continue
            if not arr or backet_map[arr.pop()] != x:
                return False
        if len(arr) != 0:
            return False
        return True


s = Solution()

print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([)]"))
print(s.isValid("{[]}"))
print(s.isValid("]"))