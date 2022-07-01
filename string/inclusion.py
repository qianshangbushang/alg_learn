class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        delta = [0] * 26
        for x in s1:
            delta[ord(x) - ord('a')] -= 1

        slow = 0
        for fast in range(0, len(s2)):
            key = ord(s2[fast]) - ord("a")
            delta[key] += 1
            if delta[key] < 0:
                continue
            while delta[key] > 0:
                delta[ord(s2[slow]) - ord("a")] -= 1
                slow += 1
            if fast - slow + 1 == len(s1):
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.checkInclusion("ab", "afafafafba"))
