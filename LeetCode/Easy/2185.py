# Counting Words With a Given Prefix
class Solution:
    def prefixCount(self, words, pref: str) -> int:
        counter = 0 
        for i in words:
            if (i.startswith(pref)):
                counter += 1
        return counter


x = Solution()
print(x.prefixCount(["pay","attention","practice","attend"],"at"))