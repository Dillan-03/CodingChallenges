#Find First Palindromic String in the Array
class Solution:
    def firstPalindrome(self, words) -> str:
        for i in words:
            if (i == i[::-1]):
                return i[::-1]
        return ""



x = Solution()
print(x.firstPalindrome(["abc","car","ada","racecar","cool"]))