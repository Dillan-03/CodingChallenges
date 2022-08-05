# Add Binary
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        addition = bin(int(a,2) + int(b,2))
        return str(addition[addition.index("b")+1:])

x = Solution()
print(x.addBinary("11","1"))