class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or s == t:
            return False
        hash_map = [0] * 26

        for ch in s:
            hash_map[ord(ch) - ord("a")] += 1

        for ch in t:
            idx = ord(ch) - ord("a")
            hash_map[idx] -= 1
            if hash_map[idx] < 0:
                return False
        return True


if __name__ == '__main__':

    s = Solution()
    print(s.isAnagram("rat", "cat"))
    print(s.isAnagram("anagram", "nagaram"))
