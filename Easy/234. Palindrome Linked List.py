#Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        
        #Find the midpoint via two pointer
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #Reverse
        prev = None
        curr = slow
        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
        
        head_ref = head
        reverse_ref = prev
        while reverse_ref:
            if head_ref.val != reverse_ref.val:
                return False
            head_ref = head_ref.next
            reverse_ref = reverse_ref.next
        
        return True
