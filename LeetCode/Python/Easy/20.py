# Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) % 2 != 0:
            return False
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif i == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            elif i == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
        return len(stack) == 0

x = Solution()
print(x.isValid('(){}{}'))
