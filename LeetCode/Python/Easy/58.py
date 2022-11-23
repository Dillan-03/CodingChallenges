class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        return len(s[-1])


x = Solution()
print(x.lengthOfLastWord("Hello    World   "))