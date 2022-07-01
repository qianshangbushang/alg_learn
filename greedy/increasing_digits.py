class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        x = 0
        base = 1
        while n > 0:
            if n % 10 > (n // 10) % 10:
                x =  x  + n % 10 * base
                n = n // 10
                base *= 10
                continue


            

        return x
