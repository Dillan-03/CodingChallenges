# Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        s = (list(s))
        letter = 0
        counter = 0
        while letter+1 < len(s):
            if (s[letter] == '(' and s[letter+1] == ')'):
                counter +=1 
            if (s[letter] == '{' and s[letter+1] == '}'):
                counter +=1
            if (s[letter] == '[' and s[letter+1] == ']'):
                counter +=1
         
            letter += 1
        # print(counter)
        # return False

x = Solution()
print(x.isValid('(){}}{'))