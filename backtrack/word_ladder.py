#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :word_ladder.py
# @Time      :2022/11/8 16:59


from collections import defaultdict
from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def create_map(all_words: List[str]):
            # word_dict = {}
            link_list = defaultdict(list)
            for word in all_words:
                # word_dict[word] = len(word_dict)
                for r in [word[:i] + "*" + word[i + 1:] for i in range(len(word))]:
                    # word_dict[r] = len(word_dict)
                    link_list[word].append(r)
                    link_list[r].append(word)
            return link_list

        relation = create_map(wordList + [beginWord])
        dq, used = deque(), set()
        dq.append((beginWord, 0))
        used.add(beginWord)
        while len(dq) > 0:
            node, depth = dq.popleft()
            for next in relation[node]:
                if next == endWord:
                    return (depth + 1) // 2 + 1
                if next in used:
                    continue
                dq.append((next, depth + 1))
                used.add(next)
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
