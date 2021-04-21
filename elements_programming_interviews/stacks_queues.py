# stacks: last in, first out
# queues: first in, first out

"""
stacks support two basic operations- push and pop. elements are added and removed in last-in, first-out order.
if stack is empty, pop usually returns null or throws an exception

when the stack is implemented using a linked list, these operations have O(1) time complexity. If it is implements using an array, there is maximum number of entries it can have,
push and pop are still O(1).
"""

# use a stack to print the entries of a singly-linked list in reverse order

def print_linked_list_in_reverse(head):
  nodes = []
  while head:
    nodes.append(head.data)
    head = head.next
  while nodes:
    print(nodes.pop())

# implement a stack with max API
# design a stack that includes a max operation, in addition to push and pop. The max method should return the maximum value stored in the stack

class Stack:
  ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax', ('element', 'max'))

  def __init__(self):
    self._element_with_cached_max = []

  def empty(self):
    return len(self._element_with_cached_max) == 0

  def max(self):
    if self.empty():
      raise IndexError('max(): empty stack')
    return self._element_with_cached_max[-1].max

  def pop(self):
    if self.empty():
      raise IndexError('pop(): empty stack')
    return self._element_with_cached_max.pop().element

  def push(self, x):
    self._element_with_cached_max.append(
      self.ElementWithCachedMax(x, x
                                if self.empty() else max(x, self.max())))
