# Number of Strings That Appear as Substrings in Word
class Solution:
    def numOfStrings(self, patterns, word: str) -> int:
        counter = 0
        for string in patterns:
            if string in word:
                counter += 1
        return counter

x = Solution()
print(x.numOfStrings(["a","abc","bc","d"]))