# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def rotateRight(self, A, B):
        
        for _ in range(B):
            extra = A.val
            node = A.next
            while(node):
                temp = node.val
                node.val = extra
                extra = temp
                node = node.next
            A.val = extra
        return A