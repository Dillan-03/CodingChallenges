#Valid Palindrome
import re
def isPalindrome(s):
    holder = re.sub(r'[^a-zA-Z0-9]', '',s)
    return holder.lower() == holder[::-1].lower()
    
print(isPalindrome('"A man, a plan, a canal: Panama"'))