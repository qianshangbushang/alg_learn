#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :word_break.py
# @Time      :2022/7/3 23:04


from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        s -> 背包
        wordDict -> 物品

        dp[i] 字符串长度为i时是否可拆分

        dp[0] = True
        dp[i] = dp[i - len(word)]
        :param s:
        :param wordDict:
        :return:
        """

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i < len(word):
                    continue
                if word != s[i - len(word):i]:
                    continue
                dp[i] = dp[i] or dp[i - len(word)]
        return dp[len(s)]


if __name__ == '__main__':
    s = Solution()
    # print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    # print(s.wordBreak("leetcode", ["leet", "code"]))
    print(s.wordBreak("dogs", ["dog", "s", "gs"]))
