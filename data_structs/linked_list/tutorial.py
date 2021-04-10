"""
A linked list is a data structure made of a chain of node objects. Each node
contains a value and a pointer to the next node in the chain.
Linnked lists are preferred over arrays due to their dynamic size and ease of
insertion and deletion properties. 
"""

# Make a single node
class Node:
  # constructor
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

# Joining nodes containing data using next pointers with single head, singly linked list
class SinglyLinkedList:
  def __init__(self):
    self.head = None

# print linked list
  def printlist(self):
    printval = self.head
    while printval != None:
      print(printval.data)
      printval = printval.next

# add elements from the tail
  def insert_tail(self, newdata):
    newNode = Node(newdata)
    if self.head == None:
      self.head = newNode
      return
    last = self.head
    while(last.next):
      last = last.next
    last.next = newNode

SLL = SinglyLinkedList()
SLL.head = Node("mon")
tuesday = Node("tues")

SLL.head.next = tuesday
SLL.insert_tail("wednes")
print("SINGLY LINKED LIST")
SLL.printlist()
