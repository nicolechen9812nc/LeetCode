#Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

class Solution(object):
    def deleteDuplicates(self, head):
        value=head
        while value and value.next:
            if value.val==value.next.val:
                value.next=value.next.next
            else:
                value=value.next
        return head
