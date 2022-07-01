class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        delta = [0] * 128

        slow = 0
        max_len = 0
        for fast in range(len(s)):
            index = ord(s[fast]) - ord("a")
            delta[index] += 1

            while delta[index] > 1:
                sindex = ord(s[slow]) - ord("a")
                delta[sindex] -= 1
                slow += 1
            max_len = max(fast - slow + 1, max_len)
        return max_len

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("pwwkew"))
