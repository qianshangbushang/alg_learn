# -*- coding: utf-8 -*-
# @Time    : 2020/9/30 21:09

"""
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/queue-stack/kfgtt/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
import math


class Solution:
    def numSquares(self, n: int) -> int:
        # 1, 4, 9, 16, 25 ...
        # 1, 4, 9, 16, 25 ... 2, 5,
        end = math.sqrt(n)
        x = []
        visited = set()
        for i in range(int(end) + 1):
            if i * i == n:
                return 1
            else:
                x.append((i * i, 1))
                visited.add((i * i, 1))
        while x:
            base, level = x[0]
            x = x[1:]
            for i in range(int(end) + 1):
                if base + i * i == n:
                    return level + 1
                elif base + i * i < n:
                    if (base + i * i, level + 1) not in visited:
                        x.append((base + i * i, level + 1))
                        visited.add((base + i * i, level + 1))
                else:
                    break
        return -1


s = Solution()

print(s.numSquares(12))
print(s.numSquares(13))
