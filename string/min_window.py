from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""
        delta = defaultdict(int)
        for ch in t:
            delta[ch] -= 1
        negative_cnt = len(delta)

        slow = 0
        result = ""
        for fast in range(len(s)):
            if s[fast] not in delta:
                continue
            delta[s[fast]] += 1
            if delta[s[fast]] == 0:
                negative_cnt -= 1
            if negative_cnt > 0:
                continue

            while slow < fast:
                if s[slow] not in delta:
                    slow += 1
                    continue
                if delta[s[slow]] <= 0:
                    break
                delta[s[slow]] -= 1
                slow += 1
            if not result or len(result) > fast - slow +1:
                result = s[slow:fast +1]
            delta[s[slow]] -= 1
            slow += 1
            negative_cnt += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("a", "B"))
