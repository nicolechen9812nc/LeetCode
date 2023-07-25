#Given the head of a singly linked list, reverse the list, and return the reversed list.
class Solution(object):
    def reverseList(self, head):
        prev = None

        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt

        return prev
        
