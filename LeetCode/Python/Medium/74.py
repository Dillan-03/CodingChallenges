# 74. Search a 2D Matrix
class Solution:
    def searchMatrix(matrix, target):

        for i in matrix:
            for j in range(0, len(i)):
                if i[j] == target:
                    return True
        return False


print(Solution.searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
