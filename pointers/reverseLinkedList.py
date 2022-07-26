# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
          # Save pointer to next item before we break link
          nxt = curr.next

          # reverse current node pointer (breaking link)
          curr.next = prev

          # move both previous and curr forward one node
          prev = curr
          curr = nxt

        # prev contains head of reversed list once iteration terminates 
        return prev  

# ==============================================

  # Helper method recursion
  def reverseListRecursive(self, head):

    def reverse(cur, prev):
      if cur is None:
        return prev
      else:
        next = cur.next
        cur.next = prev
        return reverse(next, cur)

    return reverse(head, None)

# ==============================================

  # Pure Recursive solution
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

    #  Base case where we reach the end of the original list
    if not head:
      return None

    newHead = head

    # Case where we can continue recursing since terminal case not reached
    if(head.next):
      newHead = self.reverseList(next.head)
      head.next.next = head

    head.next = None

    return newHead

# ==============================================

