# Group Anagrams
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):

        holder = defaultdict(list)
        for item in strs:
            holder[str(sorted(item))].append(item)

        return (list(holder.values()))


x = Solution()
print(x.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
