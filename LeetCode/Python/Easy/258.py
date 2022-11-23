class Solution:
    def addDigits(self, num: int) -> int:
        num = [int(x) for x in str(num)]
        while sum(num ) > 9:
            num = [int(x) for x in str(sum(num))]
           
        print(sum(num))


x = Solution()
print(x.addDigits(1119))