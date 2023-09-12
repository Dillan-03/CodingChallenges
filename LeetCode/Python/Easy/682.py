# Baseball Game
class Solution:
    def calPoints(self, operations):
        score = []
        for i in operations:
            if i == "C":
                score.pop()
            elif i == "D":
                score.append(score[-1]*2)
            elif i == "+":
                score.append(score[-1]+score[-2])
            else:
                score.append(int(i))
        return sum(score)


x = Solution()
print(x.calPoints(["5", "2", "C", "D", "+"]))
