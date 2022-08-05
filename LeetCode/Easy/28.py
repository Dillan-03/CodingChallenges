# Implement strStr()
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except ValueError:
            return -1

x = Solution()
print(x.strStr("hello","p"))