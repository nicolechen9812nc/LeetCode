#Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

class Solution(object):
    def removeElements(self, head, val):
        new = ListNode(0)
        new.next=head

        curr=new
        while curr.next!=None:
            if curr.next.val==val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return new.next
