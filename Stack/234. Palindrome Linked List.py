#Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

class Solution(object):
    def isPalindrome(self, head):
        stack = [];
        left = head
        right = head
        
        while right:
            stack.append(right.val)
            right = right.next 
                
        while left:
            if left.val == stack.pop(): 
                left = left.next
            else:
                return False 
        
        return True
        
