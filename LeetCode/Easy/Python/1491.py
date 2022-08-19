# Average Salary Excluding the Minimum and Maximum Salary
class Solution:
    def average(self, salary):
        salary.sort()
        del salary[0]
        del salary[-1]
        return(sum(salary)/len(salary))


x = Solution()
print(x.average([4000,3000,2000,1000]))
        