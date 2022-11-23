# Occurences after bigram
class Solution:
    def findOcurrences(self, text: str, first: str, second: str):
        occ = []
        words = list(text.split())
        checker = 0
        while checker+2 < len(words):
            if ((words[checker] == first) and (words[checker+1] == second)):
                occ.append(words[checker+2])
            checker += 1
        return occ
        


x = Solution()
print(x.findOcurrences(text = "alice is a good girl she is a good student", first = "a", second = "good"))