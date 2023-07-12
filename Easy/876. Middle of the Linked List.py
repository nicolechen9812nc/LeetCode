#Given the head of a singly linked list, return the middle node of the linked list.

#If there are two middle nodes, return the second middle node.

class Solution(object):
    def middleNode(self, head):
        nodes = []
        while head:
            nodes.append(head)
            head=head.next
        middle=len(nodes)//2
        return (nodes[middle])
