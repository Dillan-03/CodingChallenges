#Convert Binary Number in a Linked List to Integer

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        holder = []
        while head: #while it reads the head until it reaches the end
            holder.append(str(head.val))
            head= head.next
        binary = ''.join(holder)
        return int(binary,2)

x=Solution()
print(x.getDecimalValue([1,0,1]))