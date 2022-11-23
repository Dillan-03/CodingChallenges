class Solution:
    def mergeTwoLists(self, list1, list2):
        for x in range(0,len(list2)):
            list1.append(list2[x])
        list1.sort()
        return list1

x = Solution()
print(x.mergeTwoLists([1,2,4],[1,3,4]))