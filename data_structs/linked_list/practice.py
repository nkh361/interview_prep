# Bonus problem || https://leetcode.com/problems/linked-list-cycle/

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class CircularLL:
  def __init__(self):
    self.head = None

  def insert(self, data):
    newNode = Node(data)
    curr = self.head
    newNode.next = self.head #loops last ptr to first node
    
    # if linked list is not None then set next of last node
    if self.head != None:
      while(curr.next != self.head):
        curr = curr.next
      curr.next = newNode
    else:
      newNode.next = newNode # for the first node
    self.head = newNode

  def printList(self):
    curr = self.head
    count = 0
    if self.head != None:
      while(True):
        print("index: {}".format(count))
        print("data: {}".format(curr.data))
        curr = curr.next
        count+=1
        if curr == self.head:
          break #avoid infinite loop

cll = CircularLL()

cll.insert(1)
cll.insert(4)
cll.insert(6)
cll.insert(8)

cll.printList()

