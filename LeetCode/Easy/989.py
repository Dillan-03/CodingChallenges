from posixpath import split


class Solution:
    def addToArrayForm(self, num, k: int):

        # convert to int
        numbers = int("".join(map(str, num)))

        nums = (numbers) + k
        # convert back to list int
        nums = [int(x) for x in str(nums)]

        return nums

x = Solution()
print(x.addToArrayForm([1,2,0,0],34))