class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    cnt += 1
        return cnt

    def is_palindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


class Solution:
    def countSubstrings(self, s: str) -> int:
        ret = 0
        for idx in range(len(s)):
            ret += self.cnt_pal(s, idx, idx)
            ret += self.cnt_pal(s, idx, idx + 1)
        return ret

    def cnt_pal(self, s, left, right):
        cnt = 0
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
            cnt += 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.countSubstrings("abc"))
    # print(s.is_palindrome("aaa", 1, 2))
