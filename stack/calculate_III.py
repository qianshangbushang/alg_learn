#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :calculate_III.py
# @Time      :2022/7/16 9:31


class Solution:
    def calculate(self, s: str) -> int:
        result, _ = self.parseExpr(s, 0)
        return result

    def parseExpr(self, s: str, start: int):
        data = []
        i, last_op = start, '+'

        while i < len(s) and s[i] not in [')', '}', ']']:
            if s[i] == ' ':
                i += 1
                continue
            # 到这里的只能是字符和括号
            if s[i] in ['(', '{', '[']:
                num, i = self.parseExpr(s, i + 1)
            else:
                num, i = self.parseNum(s, i)

            if last_op == "+":
                data.append(num)
            if last_op == "-":
                data.append(-num)
            if last_op == "*":
                data[-1] *= num
            if last_op == "/":
                data[-1] = int(data[-1] / num)

            if i < len(s) and s[i] not in [')', '}', ']']:
                last_op = s[i]
                i += 1

        return sum(data), i + 1

    def parseNum(self, s: str, start: int):
        i, num = start, 0
        while i < len(s) and '0' <= s[i] <= '9':
            num = num * 10 + ord(s[i]) - ord('0')
            i += 1
        return num, i


if __name__ == '__main__':
    s = Solution()
    # print(s.parseNum("1231+f", 0))
    print(s.calculate("(2+6* 3+5- (3*14/7+2)*5)+3"))
    print(s.calculate("2*(5+5*2)/3+(6/2+8)"))
