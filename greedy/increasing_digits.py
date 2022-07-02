#  1324
#  1299

#  23324523
#  23324499 -> 2329999 -> 2299999

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        x = self.split_n(n)

        idx = 0
        while idx < len(x) - 1:
            if x[idx + 1] > x[idx]:
                x[idx + 1] -= 1
                x[:idx + 1] = [9] * (idx + 1)
            idx += 1

        return sum([x[idx] * (10 ** idx) for idx in range(len(x))])

    def split_n(self, n):
        ret = []

        while n > 0:
            ret.append(n % 10)
            n = n // 10
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.monotoneIncreasingDigits(323))
