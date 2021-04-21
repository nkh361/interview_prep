# a singly linekd list is a data structure that contains a sequence of nodes such that each node contains an object and reference to the next node in the list

# each node in this example has two entries, a data field and a next field

class Node:
  def __init__(self, data=0, next_node=None):
    self.data = data
    self.next = next_node

  # search for a key:
  def search_list(L, key):
    while L and L.data != key:
      L = L.next
    # if key was not present in the list, L becomes null
    return L

  # insert a new node after node
  def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node

  # delete the node past this one, assume node is not a tail
  def delete_after(node):
    node.next = node.next.next

"""
- List problems ofter have a simple brute-force solution that uses O(n) space, but a subtler solution that uses the existing list nodes to reduce space
  complexity to O(1)

- Very often, a problem on lists is conceptually simple, and is more about cleanly coding whats specified, rather than designing an algorithm

- Consider using a dummy head to avoid having to check for empty lists, this simplifies code, makes bugs less likely
"""


# test for cyclicity #
# Write a program that takes the head of a singly linked list and returns null if there does not exist a cycle, and the node at the start of the cycle, if a cycle is present.

def has_cycle(head):
  def cycle_len(end):
    start, step = end, 0
    while True:
      step += 1
      start = start.next
      if start is end:
        return step
  fast = slow = head
  while fast and fast.next and fast.next.next:
    slow, fast = slow.next, fast.next.next
    if slow is fast:
      # Finds the start of the cycle
      cycle_len_advanced_iter = head
      for _ in range(cycle_len(slow)):
        cycle_len_advanced_iter = cycle_len_advanced_iter.next
      it = head
      # both iterators advance in tandem
      while it is not cycle_len_advanced_iter:
        it = it.next
        cycle_len_advanced_iter = cycler_len_advanced_iter.next
      return it   # iter is the start of the cycle
  return None   # No cycle
















