#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :satisfy_equality.py
# @Time      :2023/1/17 9:07


from typing import List

"""
给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，
并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。

只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false

输入：["a==b","b!=a"]
输出：false
解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程
"""


class Recorder:
    def __init__(self):
        self.father = {}

    def find(self, x):
        if self.father[x] == x:
            return x
        return self.find(self.father[x])

    def merge(self, x, y):
        self.father[self.find(y)] = self.find(x)
        return


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        recorder = Recorder()
        father_dict = {}
        for eq in equations:
            father_dict[eq[0]] = eq[0]
            father_dict[eq[3]] = eq[3]
        recorder.father = father_dict

        equations.sort(key=lambda x: x[1], reverse=True)
        for eq in equations:
            if eq[1] == "!":
                if recorder.find(eq[0]) == recorder.find(eq[3]):
                    return False
            else:
                recorder.merge(eq[0], eq[3])
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.equationsPossible(["a==b", "b!=a"]))
    print(s.equationsPossible(["a==b", "b==c", "a!=c"]))
    print(s.equationsPossible(["a==b", "b==c", "a==c"]))
    print(s.equationsPossible(["a!=a"]))
    print(s.equationsPossible(["c==c", "f!=a", "f==b", "b==c"]))
    print(s.equationsPossible(["a==b", "b!=c", "c==a"]))
    print(s.equationsPossible(["a!=b", "b!=c", "c!=a"]))
