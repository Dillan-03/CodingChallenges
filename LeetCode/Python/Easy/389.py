class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
       
        for letter in t:
            if letter not in s:
                return letter
x = Solution()
print(x.findTheDifference("","y")) 