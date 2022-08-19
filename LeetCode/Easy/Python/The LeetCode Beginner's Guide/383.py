# Ransom Note
from typing import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        holderOne = Counter(ransomNote)
        holderTwo = Counter(magazine)
        for letter in holderOne:
            if (holderOne[letter] > holderTwo[letter]):
                return False
        return True
x = Solution()
print(x.canConstruct("aa","ab"))