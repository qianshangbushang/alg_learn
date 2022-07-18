#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :is_match.py
# @Time      :2022/7/18 10:21


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        dp[i][j] 表示 p[:i] 与 s[:j]匹配情况

        如果 p[i] == "*": dp[i][j] = dp[i-1][j] or dp[i][j-1], dp[i-1][j] 即删除*号, dp[i][j-1] 即删除s[j]
        如果 p[i] == "?": dp[i][j] = dp[i-1][j-1]  一定匹配上

        其他情况： dp[i][j] = dp[i-1][j-1] and p[i] == s[j]
        :param s:
        :param p:
        :return:
        """
        dp = [[False for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]
        dp[0][0] = True

        for i in range(1, len(p) + 1):
            if p[i - 1] == "*":
                dp[i][0] = dp[i - 1][0]

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] == "*":
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                    continue
                if p[i - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                    continue

                dp[i][j] = dp[i - 1][j - 1] and p[i - 1] == s[j - 1]
                # if not dp[i][j]:
                #     return False
        # print(*dp, sep='\n')
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    # print(s.isMatch("aa", "a"))
    # print(s.isMatch("aa", "*"))
    print(s.isMatch("adceb", "*a*b"))
    print(s.isMatch("acdcb", "a*c?b"))
    print(s.isMatch("", "***"))
