# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 23:36
# @Author  : chaucerhou
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x in ["+", "-", "*", "/"]:
                a = stack.pop()
                b = stack.pop()
                stack.append(self.compute(b, a, x))
            else:
                stack.append(int(x))
            print(1, stack)

        while len(stack) > 1:
            print(2, stack)
            op = stack.pop()
            a = stack.pop()
            b = stack.pop()
            stack.append(self.compute(b, a, op))

        return stack[-1]

    def compute(self, a, b, x):
        if x == "+":
            return a + b
        if x == "-":
            return a - b
        if x == "*":
            return a * b
        if x == "/":
            return int(a / b)

s = Solution()
print(s.evalRPN(["2", "1", "+", "3", "*"]))
print(s.evalRPN(["4", "13", "5", "/", "+"]))
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
