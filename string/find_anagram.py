from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        delta = [0] * 26
        for x in p:
            delta[ord(x) - ord("a")] -= 1

        result = []
        slow = 0
        for fast in range(len(s)):
            findex = ord(s[fast]) - ord("a")
            delta[findex] += 1
            # print(delta)
            if delta[findex] < 0:
                continue

            while delta[findex] > 0:
                sindex = ord(s[slow]) - ord("a")
                delta[sindex] -= 1
                slow += 1

            if fast - slow == len(p) - 1:
                result.append(slow)
                delta[ord(s[slow]) - ord("a")] -= 1
                slow += 1


        return result


if __name__ == '__main__':
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))
