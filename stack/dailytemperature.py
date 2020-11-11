# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 23:01
# @Author  : chaucerhou
from typing import List

"""
所谓单调栈就是在栈先进后出的特性之外再添加一个特性：从栈顶到栈底的元素严格递增（or递减）。

栈内元素保持单调，有单调递增栈和单调递减栈。注意：这里的单调递增或递减指的是从栈顶到栈底单调递增或递减。
每个元素都要入栈，且仅入栈一次，出栈后不再入栈。
注意：栈内可以直接存储元素，也可以存储元素的索引，一般存储的是索引。当存储的是索引时，是说索引对应的元素是单调的，而不是说索引是单调的。
操作规则（以单调递增栈为例，单调递减栈相反）：设当前进栈元素为 e，如果 e 小于栈顶元素，就直接入栈；如果 e 大于或等于栈顶元素，那就一直弹栈，直到栈顶元素大于 e 或者栈为空时，再将 e 入栈。

利用单调递增栈，我们能找到栈顶元素左右两边第一个大于该栈顶元素的元素；
利用单调递减栈，我们能找到栈顶元素左右两边第一个小于该栈顶元素的元素。

"""
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = list()
        res = [0 for x in T]
        for idx, x in enumerate(T):
            if len(stack) == 0:
                stack.append(0)
                continue
            while len(stack) > 0 and x > T[stack[-1]] :
                pos = stack.pop()
                res[pos] = idx - pos

            stack.append(idx)
        for x in stack:
            res[x] = 0
        return res

s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
