class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(filter(str.isalnum, s.lower()))
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_valid(x, left, right, cnt):
            while x[left] == x[right] and left < right:
                left += 1
                right -= 1

            if left >= right:
                return True

            if cnt == 0:
                return False

            s1 = is_valid(x, left, right - 1, cnt - 1)
            s2 = is_valid(x, left + 1, right, cnt - 1)
            return s1 or s2

        return is_valid(s, 0, len(s) - 1, 1)


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1

        if left >= right:
            return True

        return self.isValid(s, left, right - 1) or self.isValid(s, left + 1, right)

    def isValid(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.validPalindrome("ebcbbececabbacecbbcbe"))
