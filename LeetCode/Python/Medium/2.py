# Add Two Numbers

# Definition of a node in a linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution class
class Solution:
    # Method to add two numbers represented as linked lists
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a new linked list to store the result
        holder = ListNode()
        current = holder

        # Initialize carry to 0
        carry = 0

        # Iterate through the linked lists and add the corresponding nodes
        while l1 or l2 or carry:
            # If l1 has a node, get its value; otherwise, set it to 0
            d1 = l1.val if l1 else 0
            # If l2 has a node, get its value; otherwise, set it to 0
            d2 = l2.val if l2 else 0

            # Add the values of the nodes and the carry from the previous calculation
            val = d1 + d2 + carry

            # Update the carry for the next calculation
            carry = val // 10

            # Get the remainder (single digit) for the current node value
            val = val % 10

            # Create a new node with the calculated value
            current.next = ListNode(val)

            # Move the current pointer to the next node
            current = current.next

            # Move l1 and l2 to the next nodes if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the result (linked list starting from the second node)
        return holder.next
